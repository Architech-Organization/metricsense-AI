from abc import abstractmethod


class SummaryService:

    @abstractmethod
    def generate_summary_for_engineering(self, type: str,text: str) -> str:
        pass