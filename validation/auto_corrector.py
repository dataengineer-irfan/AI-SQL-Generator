from validation.sql_validator import SQLValidator
from validation.dataset_validator import DatasetValidator


class AutoCorrector:

    def __init__(self):

        self.oracle_validator = SQLValidator()

        self.dataset_validator = DatasetValidator()

    def validate(
        self,
        sql: str
    ):

        sql_upper = sql.upper()

        # Dataset SQL
        if "SALES_DATA_SAMPLE" in sql_upper:

            return self.dataset_validator.validate(
                sql
            )

        # Oracle SQL
        return self.oracle_validator.validate(
            sql
        )