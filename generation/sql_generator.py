from generation.prompt_builder import PromptBuilder
from generation.sql_cleaner import SQLCleaner

from providers.groq_provider import GroqProvider

from rag.rag_pipeline import RAGPipeline


class SQLGenerator:

    def __init__(self):

        self.provider = GroqProvider()

        self.rag = RAGPipeline()

    def generate(
        self,
        question: str,
        schema_context: str | None = None
    ) -> str:

        if not schema_context:

            schema_context = (
                self.rag.retrieve(
                    question,
                    top_k=4
                )
            )

        prompt = (
            PromptBuilder.build(
                question,
                schema_context
            )
        )

        response = (
            self.provider.generate(
                prompt,
                temperature=0.0
            )
        )

        return SQLCleaner.clean(
            response
        )