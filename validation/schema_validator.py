import re

from database.schema_extractor import SchemaExtractor


class SchemaValidator:

    def __init__(self):

        self.extractor = SchemaExtractor()

        self.schema = (
            self.extractor.extract_schema()
        )

        self.tables = {
            table.upper(): table_data
            for table, table_data in self.schema.items()
        }

    def validate(
        self,
        sql: str
    ):

        issues = []

        sql_upper = sql.upper()

        table_pattern = (
            r"\bFROM\s+([A-Z_0-9]+)|"
            r"\bJOIN\s+([A-Z_0-9]+)"
        )

        matches = re.findall(
            table_pattern,
            sql_upper
        )

        tables = []

        for from_table, join_table in matches:

            if from_table:
                tables.append(from_table)

            if join_table:
                tables.append(join_table)

        for table in tables:

            if table not in self.tables:

                issues.append(
                    f"Unknown table: {table}"
                )

        return {
            "valid": len(issues) == 0,
            "issues": issues
        }
