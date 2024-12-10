from fastapi import APIRouter, HTTPException, Query
from src.generate_summary.summary_factory import SummaryFactory
from src.services.board_issue_service import BoardIssueService
from src.utils.metric_type import MetricType

class EngineeringRouter:
    def __init__(self, summary_factory: SummaryFactory, board_issue_service: BoardIssueService):
        self.board_issue_service = board_issue_service
        self.summary_factory = summary_factory
        self.router = APIRouter(
            prefix="/v1/engineering", tags=["engineering"]
        )
        self.router.get("/healthcheck")(self.healthcheck)
        self.router.get("/engineeringSummary")(self.engineering_summary)

    async def healthcheck(self):
        try:
            return {"status": "Application Up"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def engineering_summary(self, type: str = Query(...), project: str = Query(...), priority: str = Query(...), month: str = Query(...)):
        try:
            data = await self.board_issue_service.read_board_issues(type, project, priority, month)
            summary_service = self.summary_factory.create_summary(self.summary_factory.service_name)
            summary = summary_service.generate_summary_for_engineering(type, data)
            return {"summary": summary}

        except Exception as e:
            return {"error": str(e)}