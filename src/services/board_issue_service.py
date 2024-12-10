from src.utils.metric_type import MetricType

class BoardIssueService:
    def __init__(self, database):
        self.database = database

    async def read_board_issues(self, type:str, project: str, priority: str, month: str):
        if project.lower() == "all":
            project_condition = "pm.project_name IN ('Demo','Demo-2','GS1-Demo','GS1-Sandbox','KT','demo-3','test')"
        else:
            project_condition = f"pm.project_name IN ('{project}')"
        if priority.lower() == "all":
            priority_condition = "i.priority IN ('', 'Medium')"
        else:
            priority_condition = f"i.priority IN ('{priority}')"
        month = f"{month}-01"

        query = ""
        match type:
            case MetricType.DEFECTS.value:
                query = f"""
                SELECT count(*) as count
                FROM lake.issues i
                JOIN board_issues bi ON i.id = bi.issue_id
                JOIN boards b ON bi.board_id = b.id
                JOIN project_mapping pm ON b.id = pm.row_id
                WHERE {project_condition}
                  AND {priority_condition}
                  AND i.type = 'BUG'
                  AND DATE(i.created_date) BETWEEN STR_TO_DATE('{month}', '%Y-%m-%d')
                  AND STR_TO_DATE('{month}', '%Y-%m-%d') + INTERVAL 1 MONTH - INTERVAL 1 DAY;"""
            case MetricType.DEV_COUNT.value:
                query = f"""
                select
                count(distinct author_name) as count
                from
                lake.commits c
                join lake.repo_commits rc on c.sha = rc.commit_sha
                join project_mapping pm on rc.repo_id = pm.row_id
                where
                date(authored_date) between
                    STR_TO_DATE('{month}','%Y-%m-%d') and
                    STR_TO_DATE('{month}','%Y-%m-%d') + INTERVAL 1 MONTH - INTERVAL 1 DAY and
                    {project_condition};
                """

        return await self.database.fetch_all(query)
