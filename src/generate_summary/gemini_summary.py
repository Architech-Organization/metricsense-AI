from src.generate_summary.summary_service import SummaryService
from google.cloud import aiplatform

class GeminiSummary(SummaryService):

    def generate_summary_for_critical_defects_identified(self, text: str) -> str:

        # Create a Text Generation model instance
        model = aiplatform.TextGenerationModel.from_pretrained("text-bison@001")

        # Generate the summary
        response = model.predict(
            text,
            temperature=0.7,
            max_output_tokens=150,
            top_p=0.8,
            top_k=40
        )

        # Return the generated text
        return response.text