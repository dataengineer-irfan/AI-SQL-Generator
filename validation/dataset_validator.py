import re

from kaggle_integration.metadata_indexer import MetadataIndexer


class DatasetValidator:

    def __init__(self):

        indexer = MetadataIndexer()

        metadata = indexer.build_metadata(
            "datasets"
        )

        self.tables = set()

        self.columns = {}

        for item in metadata:

            table_name = (
                item["file"]
                .replace(".csv", "")
                .replace("-", "_")
                .upper()
            )

            self.tables.add(
                table_name
            )

            self.columns[table_name] = {
                column.upper()
                for column in item["columns"]
            }

    def validate(
        self,
        sql: str
    ):

        issues = []

        sql_upper = sql.upper()

        # ----------------------------
        # Validate Tables
        # ----------------------------

        table_pattern = (
            r"\bFROM\s+([A-Z0-9_]+)|"
            r"\bJOIN\s+([A-Z0-9_]+)"
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
                    f"Dataset table does not exist: {table}"
                )

        # ----------------------------
        # Alias Validation
        # ----------------------------

        oracle_keywords = {
            "SELECT", "FROM", "WHERE",
            "GROUP", "ORDER", "BY",
            "HAVING", "JOIN",
            "INNER", "LEFT",
            "RIGHT", "FULL",
            "ON", "AS",
            "AND", "OR",
            "NOT", "NULL",
            "IN", "IS",
            "LIKE", "BETWEEN",
            "UNION", "ALL",
            "DISTINCT",
            "CASE", "WHEN",
            "THEN", "ELSE",
            "END",
            "SUM", "COUNT",
            "AVG", "MIN",
            "MAX",
            "FETCH", "FIRST",
            "ROWS", "ONLY"
        }

        alias_map = {}

        alias_pattern = (
            r"(?:FROM|JOIN)\s+([A-Z0-9_]+)\s+(?:AS\s+)?([A-Z0-9_]+)"
        )

        matches = re.findall(
            alias_pattern,
            sql_upper
        )

        for table, alias in matches:

            if alias in oracle_keywords:

                issues.append(
                    f"Invalid alias '{alias}' (Oracle keyword)"
                )

            else:

                alias_map[alias] = table

        alias_usage = set(
            re.findall(
                r"\b([A-Z][A-Z0-9_]*)\.",
                sql_upper
            )
        )

        for alias in alias_usage:

            if alias in oracle_keywords:
                continue

            if alias not in alias_map:

                issues.append(
                    f"Unknown alias: {alias}"
                )

        # ----------------------------
        # Validate Columns
        # ----------------------------

        if referenced_tables:

            table = referenced_tables[0]

            if table in self.columns:

                valid_columns = (
                    self.columns[table]
                )

                select_match = re.search(
                    r"SELECT(.*?)FROM",
                    sql_upper,
                    re.DOTALL
                )

                if select_match:

                    select_text = (
                        select_match.group(1)
                    )

                    standalone = re.findall(
                        r"\b[A-Z][A-Z0-9_]*\b",
                        select_text
                    )

                    ignore = {
                        "SUM",
                        "AVG",
                        "COUNT",
                        "MIN",
                        "MAX",
                        "DISTINCT",
                        "AS",
                        "CASE",
                        "WHEN",
                        "THEN",
                        "ELSE",
                        "END",
                        "AND",
                        "OR",
                        "NOT",
                        "NULL"
                    }

                    for col in standalone:

                        if col in ignore:
                            continue

                        if col in alias_usage:
                            continue

                        if col in alias_map:
                            continue

                        if col == table:
                            continue

                        if col.startswith(
                            "TOTAL"
                        ):
                            continue

                        if col not in valid_columns:

                            issues.append(
                                f"Unknown column: {col}"
                            )

                column_refs = re.findall(
                    r"\b[A-Z][A-Z0-9_]*\.([A-Z][A-Z0-9_]*)",
                    sql_upper
                )

                for col in column_refs:

                    if col not in valid_columns:

                        issues.append(
                            f"Unknown column: {col}"
                        )

        return {
            "valid": len(issues) == 0,
            "issues": sorted(
                set(issues)
            )
        }