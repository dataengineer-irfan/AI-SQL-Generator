import pandas as pd

from database.oracle_connector import OracleConnector


class SQLExecutor:

    def __init__(self):

        self.connector = OracleConnector()

    def execute(self, sql: str):

        sql = sql.strip()

        if sql.endswith(";"):
            sql = sql[:-1]

        connection = self.connector.connect()

        cursor = connection.cursor()

        try:

            cursor.execute(sql)

            rows = cursor.fetchall()

            columns = [
                col[0]
                for col in cursor.description
            ]

            return pd.DataFrame(
                rows,
                columns=columns
            )

        finally:

            cursor.close()

            connection.close()