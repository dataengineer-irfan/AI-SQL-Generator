import duckdb
import pandas as pd


class DatasetSQLExecutor:

    def execute(
        self,
        sql: str,
        csv_path: str
    ):

        df = pd.read_csv(
            csv_path,
            encoding="latin1"
        )

        con = duckdb.connect()

        table_name = (
            csv_path
            .split("\\")[-1]
            .replace(".csv", "")
            .upper()
            .replace("-", "_")
        )

        con.register(
            table_name,
            df
        )

        result = con.execute(
            sql
        ).fetchdf()

        return result