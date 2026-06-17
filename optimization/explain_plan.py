from database.oracle_connector import OracleConnector


class ExplainPlan:

    def __init__(self):
        self.connector = OracleConnector()

    def analyze(self, sql: str):
        sql = sql.strip()

        if sql.endswith(";"):
            sql = sql[:-1]

        connection = self.connector.connect()
        cursor = connection.cursor()

        try:
            cursor.execute(
                f"EXPLAIN PLAN FOR {sql}"
            )

            cursor.execute(
                """
                SELECT PLAN_TABLE_OUTPUT
                FROM TABLE(
                    DBMS_XPLAN.DISPLAY()
                )
                """
            )

            rows = cursor.fetchall()

            return "\n".join(
                row[0]
                for row in rows
            )

        finally:
            cursor.close()
            connection.close()
