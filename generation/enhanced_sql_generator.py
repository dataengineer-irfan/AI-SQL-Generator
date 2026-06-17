from generation.sql_generator import SQLGenerator

from kaggle_integration.dataset_context_builder import (
    DatasetContextBuilder
)


class EnhancedSQLGenerator:

    def __init__(self):

        self.sql_generator = (
            SQLGenerator()
        )

        self.dataset_context = (
            DatasetContextBuilder()
        )

    def generate(
        self,
        question,
        schema_context
    ):

        dataset_context = (
            self.dataset_context.build_context(
                question
            )
        )

        full_context = f"""
DATABASE SCHEMA

{schema_context}

DATASET KNOWLEDGE

{dataset_context}

QUESTION

{question}
"""

        return self.sql_generator.generate(
            question=question,
            schema_context=full_context
        )
