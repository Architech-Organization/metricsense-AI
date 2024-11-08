from src.generate_summary.gemini_summary import GeminiSummary
from src.generate_summary.openai_summary import OpenAISummary
from src.generate_summary.summary_service import SummaryService
from src.config import AppConfigDict

class SummaryFactory:
    def __init__(self, config: AppConfigDict):
        self.config = config
        self.service_name = config["name"]

    def create_summary(self, service_name: str) -> SummaryService:
        if service_name == "gemini":
            return GeminiSummary(self.config)
        elif service_name == "openai":
            return OpenAISummary(self.config)
        else:
            raise ValueError("Invalid summary type")