from kaggle_integration.dataset_retriever import (
    DatasetRetriever
)


class DatasetContextBuilder:

    def __init__(self):

        self.retriever = (
            DatasetRetriever()
        )

    def build_context(
        self,
        question: str
    ):

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
