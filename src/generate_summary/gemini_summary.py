from src.generate_summary.summary_service import SummaryService
import google.generativeai as genai
from src.config import AppConfigDict
from src.utils.metric_type import MetricType

class GeminiSummary(SummaryService):
    
    def __init__(self, config: AppConfigDict) -> None:
       genai.configure(api_key=config["api_key"])

    def generate_summary_for_engineering(self, type:str, text: str) -> str:
        try:
            response = ""
            count = text[0]["count"] if text else 0
            match(type):
                case MetricType.DEFECTS.value:
                                # Create a Text Generation model instance
                    model = genai.GenerativeModel(
                        model_name="gemini-1.5-flash",
                        system_instruction="""You are an insightful AI assistant tasked with summarizing engineering dashboard data.
                The provided data includes the count of critical defects identified during a specific month.
                Create a concise and engaging summary to inform the user about these critical defects,
                emphasizing their importance and the need for immediate resolution.""",
                        generation_config=genai.types.GenerationConfig(
                            # Only one response
                            candidate_count=1,
                            max_output_tokens=100,
                            temperature=1.0)
                        )
                    # Generate the summary
                    response = model.generate_content(f"Summarize the following dashboard data:\n{count}")
                case MetricType.DEV_COUNT.value:
                                # Create a Text Generation model instance
                    model = genai.GenerativeModel(
                        model_name="gemini-1.5-flash",
                        system_instruction="""You are a knowledgeable AI assistant tasked with summarizing engineering dashboard data. 
                        The provided data includes the count of developers active during a specific month. 
                        Create a concise and engaging summary to inform the user about developer count, emphasizing the importance of collaboration and productivity.""",
                        generation_config=genai.types.GenerationConfig(
                            # Only one response
                            candidate_count=1,
                            max_output_tokens=100,
                            temperature=1.0)
                        )
                    # Generate the summary
                    response = model.generate_content(f"Summarize the following dashboard data:\n{count}")
                case _:
                    return "Invalid metric type"

            return response.text
        except Exception as e:
            raise Exception(f"Error generating summary: {str(e)}")