from fastapi import FastAPI
from databases import Database
from src.config import get_app_config
from src.generate_summary.summary_factory import SummaryFactory
from src.routers.engineering_router import EngineeringRouter
from src.services.board_issue_service import BoardIssueService

config = get_app_config()
database = Database(config["database"]["url"])
app = FastAPI(
    title="Metrics AI API",
    version="v1",
)
summary_factory = SummaryFactory(config["azure_open_api"])
board_issue_service = BoardIssueService(database)
engineering_router = EngineeringRouter(summary_factory, board_issue_service)
app.include_router(engineering_router.router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
