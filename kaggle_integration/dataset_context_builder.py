from config.settings import settings

from kaggle_integration.dataset_retriever import (
    DatasetRetriever
)


class DatasetContextBuilder:

    def __init__(self):

        if settings.ENABLE_RAG:

            self.retriever = (
                DatasetRetriever()
            )

        else:

            self.retriever = None

    def build_context(
        self,
        question: str
    ):

        if not settings.ENABLE_RAG:

            return ""

        docs = self.retriever.retrieve(
            question
        )

        context = ""

        for doc in docs:

            context += (
                doc +
                "\n\n"
            )

        return context