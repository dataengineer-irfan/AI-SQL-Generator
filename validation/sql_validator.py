import re

from database.schema_extractor import SchemaExtractor


class SQLValidator:

    def __init__(self):

        self.extractor = SchemaExtractor()

        self.schema = (
            self.extractor.extract_schema()
        )

        self.tables = {
            table.upper()
            for table in self.schema.keys()
        }

        self.columns = set()

        for table_data in self.schema.values():

            for column in table_data["columns"]:

                self.columns.add(
                    column["column_name"].upper()
                )

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

        referenced_tables = []

        for from_table, join_table in matches:

            if from_table:
                referenced_tables.append(
                    from_table
                )

            if join_table:
                referenced_tables.append(
                    join_table
                )

        for table in referenced_tables:

            if table not in self.tables:

                issues.append(
                    f"Table does not exist: {table}"
                )

        valid = len(issues) == 0

        return {
            "valid": valid,
            "issues": issues
        }
