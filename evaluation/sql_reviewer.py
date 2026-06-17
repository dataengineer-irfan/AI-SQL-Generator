from providers.groq_provider import GroqProvider
from utils.sql_cleaner import SQLCleaner


class SQLReviewer:

    def __init__(self):

        self.provider = GroqProvider()

    def review(
        self,
        question: str,
        sql: str,
        score: dict,
        plan: str
    ):

        prompt = f"""
You are a senior Oracle SQL reviewer.

Return ONLY SQL.

Do not explain.
Do not use markdown.
Do not use code fences.

Question:
{question}

SQL:
{sql}

Score:
{score}

Plan:
{plan}

Review and improve SQL.
"""

        response = self.provider.generate(
            prompt,
            temperature=0.0
        )

        return SQLCleaner.clean(
            response
        )