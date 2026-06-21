from config.settings import settings

from generation.prompt_builder import PromptBuilder
from generation.sql_cleaner import SQLCleaner

from providers.groq_provider import GroqProvider


class SQLGenerator:

    def __init__(self):

        self.provider = GroqProvider()

        self.rag = None

    def _get_rag(self):

        # RAG disabled for cloud deployment
        if not settings.ENABLE_RAG:
            return None

        if self.rag is None:

            from rag.rag_pipeline import RAGPipeline

            self.rag = RAGPipeline()

        return self.rag

    def generate(
        self,
        question: str,
        schema_context: str | None = None
    ) -> str:

        if not schema_context:

            if settings.ENABLE_RAG:

                rag = self._get_rag()

                if rag is not None:

                    schema_context = rag.retrieve(
                        question,
                        top_k=4
                    )

            else:

                schema_context = ""

        prompt = PromptBuilder.build(
            question,
            schema_context
        )

        response = self.provider.generate(
            prompt,
            temperature=0.0
        )

        return SQLCleaner.clean(
            response
        )