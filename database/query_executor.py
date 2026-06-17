from typing import List
from typing import Dict
from typing import Any

from database.oracle_connector import OracleConnector


class QueryExecutor:

    def __init__(self):

        self.connector = OracleConnector()

    def execute(
        self,
        sql: str
    ) -> List[Dict[str, Any]]:

        connection = self.connector.get_connection()

        cursor = connection.cursor()

        try:

            cursor.execute(sql)

            columns = [col[0] for col in cursor.description]

            rows = cursor.fetchall()

            results = []

            for row in rows:

                results.append(
                    {
                        columns[i]: row[i]
                        for i in range(len(columns))
                    }
                )

            return results

        finally:

            cursor.close()
