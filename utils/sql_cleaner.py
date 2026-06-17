import re


class SQLCleaner:

    @staticmethod
    def clean(text: str) -> str:

        if not text:
            return ""

        text = text.strip()

        # Remove think blocks
        text = re.sub(
            r"<think>.*?</think>",
            "",
            text,
            flags=re.DOTALL | re.IGNORECASE
        )

        # Extract SQL from markdown block
        sql_block = re.search(
            r"```sql(.*?)```",
            text,
            re.DOTALL | re.IGNORECASE
        )

        if sql_block:

            sql = sql_block.group(1).strip()

        else:

            # Try finding first SELECT statement
            select_match = re.search(
                r"(SELECT[\s\S]*)",
                text,
                re.IGNORECASE
            )

            if select_match:

                sql = select_match.group(1).strip()

            else:

                sql = text

        # Remove trailing semicolon
        while sql.endswith(";"):
            sql = sql[:-1].strip()

        return sql
