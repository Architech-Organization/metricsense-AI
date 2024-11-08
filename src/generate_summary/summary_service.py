from abc import abstractmethod


class SummaryService:

    @abstractmethod
    def generate_summary_for_critical_defects_identified(self, text: str) -> str:
        pass