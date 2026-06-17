from typing import List


class PromptBuilder:

    @staticmethod
    def build(
        question: str,
        schema_context
    ) -> str:

        if isinstance(schema_context, list):

            schema_text = "\n\n".join(
                schema_context
            )

        else:

            schema_text = str(
                schema_context
            )

        return f"""
You are an expert Oracle Database Architect.

Database Schema:

{schema_text}

User Question:

{question}

Generate optimal Oracle SQL.

Requirements:

- Oracle compatible
- Correct joins
- Correct aggregations
- Use indexes where possible
- Avoid full table scans
- Avoid cartesian joins
- Production ready

Return SQL only.
"""