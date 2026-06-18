import re
import difflib

from validation.dataset_validator import DatasetValidator
from validation.sql_validator import SQLValidator


class SQLAutoCorrector:

    def __init__(self):

        self.dataset_validator = (
            DatasetValidator()
        )

        self.oracle_validator = (
            SQLValidator()
        )

        self.dataset_tables = (
            self.dataset_validator.tables
        )

        self.dataset_columns = (
            self.dataset_validator.columns
        )

    def _closest_match(
        self,
        word,
        candidates
    ):

        word = word.upper()

        candidates = list(candidates)

        # Exact match
        if word in candidates:
            return word

        # Substring match
        for candidate in candidates:

            if word in candidate:
                return candidate

            if candidate in word:
                return candidate

        # Prefix match
        for candidate in candidates:

            if candidate.startswith(word):
                return candidate

        # Fuzzy match
        matches = difflib.get_close_matches(
            word,
            candidates,
            n=1,
            cutoff=0.4
        )

        if matches:
            return matches[0]

        return word

    def _find_primary_table(
        self,
        sql
    ):

        match = re.search(
            r"\bFROM\s+([A-Z0-9_]+)",
            sql.upper()
        )

        if match:
            return match.group(1)

        return None

    def _replace_column(
        self,
        sql,
        old_column,
        new_column
    ):

        # Replace only inside SELECT clause
        select_match = re.search(
            r"SELECT(.*?)FROM",
            sql,
            flags=re.IGNORECASE | re.DOTALL
        )

        if select_match:

            select_text = (
                select_match.group(1)
            )

            new_select = re.sub(
                rf"\b{old_column}\b",
                new_column,
                select_text,
                flags=re.IGNORECASE
            )

            sql = sql.replace(
                select_text,
                new_select
            )

        # Replace only inside GROUP BY clause
        group_match = re.search(
            r"GROUP\s+BY(.*?)(ORDER\s+BY|$)",
            sql,
            flags=re.IGNORECASE | re.DOTALL
        )

        if group_match:

            group_text = (
                group_match.group(1)
            )

            new_group = re.sub(
                rf"\b{old_column}\b",
                new_column,
                group_text,
                flags=re.IGNORECASE
            )

            sql = sql.replace(
                group_text,
                new_group
            )

        return sql

    def correct(
        self,
        sql: str
    ):

        corrected_sql = sql

        for _ in range(3):

            validation = (
                self.dataset_validator.validate(
                    corrected_sql
                )
            )

            if validation["valid"]:
                break

            for issue in validation["issues"]:

                # --------------------------
                # Fix table names
                # --------------------------

                if issue.startswith(
                    "Dataset table does not exist:"
                ):

                    wrong_table = (
                        issue.split(":")[1]
                        .strip()
                    )

                    new_table = (
                        self._closest_match(
                            wrong_table,
                            self.dataset_tables
                        )
                    )

                    corrected_sql = re.sub(
                        rf"\b{wrong_table}\b",
                        new_table,
                        corrected_sql,
                        flags=re.IGNORECASE
                    )

                # --------------------------
                # Fix column names
                # --------------------------

                elif issue.startswith(
                    "Unknown column:"
                ):

                    wrong_column = (
                        issue.split(":")[1]
                        .strip()
                    )

                    table = (
                        self._find_primary_table(
                            corrected_sql
                        )
                    )

                    if (
                        table
                        and table in self.dataset_columns
                    ):

                        new_column = (
                            self._closest_match(
                                wrong_column,
                                self.dataset_columns[
                                    table
                                ]
                            )
                        )

                        corrected_sql = (
                            self._replace_column(
                                corrected_sql,
                                wrong_column,
                                new_column
                            )
                        )

        return corrected_sql