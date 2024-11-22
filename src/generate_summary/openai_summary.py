from src.generate_summary.summary_service import SummaryService
from openai import OpenAI
from src.config import AppConfigDict

class OpenAISummary(SummaryService):
    def __init__(self, config: AppConfigDict):
        self.client = OpenAI(api_key=config["api_key"])

    def generate_summary_for_engineering(self, type:str, text: str) -> str:
            try:
                count = text[0]["count(*)"] if text else 0
                response = self.client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "user",
                         "content": "You are an AI assistant that summarizes engineering dashboard data. The data"
                                    "passed in is the count of critical defects identified in the given month. "},
                        {
                            "role": "user",
                            "content": f"Summarize the following dashboard data:\n{count}"
                        }
                    ]
                ).to_dict()
                summary = response["choices"][0]["message"]["content"]
                return summary
            except Exception as e:
                raise Exception(f"Error generating summary: {str(e)}")