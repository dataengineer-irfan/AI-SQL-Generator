from providers.groq_provider import GroqProvider
from utils.sql_cleaner import SQLCleaner


class SQLOptimizer:

    def __init__(self):

        self.provider = GroqProvider()

    def optimize(
        self,
        question: str,
        sql: str,
        explain_plan: str
    ):

        prompt = f"""
You are an Oracle SQL optimization engine.

Return ONLY SQL.

No explanations.
No markdown.
No comments.

Question:
{question}

SQL:
{sql}

Execution Plan:
{explain_plan}

Optimize the query.
"""

        response = self.provider.generate(
            prompt,
            temperature=0.0
        )

        return SQLCleaner.clean(
            response
        )