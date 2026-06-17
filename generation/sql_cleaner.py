import re


class SQLCleaner:

    @staticmethod
    def clean(response: str) -> str:

        sql = response.strip()

        sql = re.sub(
            r"```sql",
            "",
            sql,
            flags=re.IGNORECASE
        )

        sql = sql.replace(
            "```",
            ""
        )

        sql = re.sub(
            r"<think>.*?</think>",
            "",
            sql,
            flags=re.DOTALL
        )

        sql = sql.strip()

        while sql.endswith(";"):
            sql = sql[:-1].strip()

        return sql