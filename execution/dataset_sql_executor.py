import os
import re

import duckdb
import pandas as pd


class DatasetSQLExecutor:

    def execute(
        self,
        sql: str,
        csv_path: str
    ):

        # -------------------------
        # Load CSV
        # -------------------------

        df = pd.read_csv(
            csv_path,
            encoding="latin1"
        )

        # -------------------------
        # Create DuckDB connection
        # -------------------------

        con = duckdb.connect()

        # -------------------------
        # Extract table name correctly
        # -------------------------

        table_name = (
            os.path.basename(csv_path)
            .replace(".csv", "")
            .replace("-", "_")
            .upper()
        )

        # -------------------------
        # Register dataframe
        # -------------------------

        con.register(
            table_name,
            df
        )

        # -------------------------
        # Convert table names to uppercase
        # -------------------------

        sql = re.sub(
            r"\bFROM\s+([A-Za-z0-9_]+)",
            lambda m: f"FROM {m.group(1).upper()}",
            sql,
            flags=re.IGNORECASE
        )

        sql = re.sub(
            r"\bJOIN\s+([A-Za-z0-9_]+)",
            lambda m: f"JOIN {m.group(1).upper()}",
            sql,
            flags=re.IGNORECASE
        )

        # -------------------------
        # Debug Output
        # -------------------------

        print("\n========== DATASET EXECUTOR ==========")
        print("CSV PATH:")
        print(csv_path)

        print("\nTABLE NAME:")
        print(table_name)

        print("\nREGISTERED TABLES:")
        print(con.execute("SHOW TABLES").fetchall())

        print("\nSQL TO EXECUTE:")
        print(sql)

        print("======================================\n")

        # -------------------------
        # Execute SQL
        # -------------------------

        result = con.execute(
            sql
        ).fetchdf()

        return result