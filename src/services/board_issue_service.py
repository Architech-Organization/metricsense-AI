class BoardIssueService:
    def __init__(self, database):
        self.database = database

    async def read_board_issues(self, project: str, priority: str, month: str):
        if project.lower() == "all":
            project_condition = "pm.project_name IN ('Demo','Demo-2','GS1-Demo','GS1-Sandbox','KT','demo-3','test')"
        else:
            project_condition = f"pm.project_name IN ('{project}')"
        if priority.lower() == "all":
            priority_condition = "i.priority IN ('', 'Medium')"
        else:
            priority_condition = f"i.priority IN ('{priority}')"
        month = f"{month}-01"

        query = f"""
                SELECT count(*)
                FROM lake.issues i
                JOIN board_issues bi ON i.id = bi.issue_id
                JOIN boards b ON bi.board_id = b.id
                JOIN project_mapping pm ON b.id = pm.row_id
                WHERE {project_condition}
                  AND {priority_condition}
                  AND i.type = 'BUG'
                  AND DATE(i.created_date) BETWEEN STR_TO_DATE('{month}', '%Y-%m-%d')
                  AND STR_TO_DATE('{month}', '%Y-%m-%d') + INTERVAL 1 MONTH - INTERVAL 1 DAY;
                """
        return await self.database.fetch_all(query)
