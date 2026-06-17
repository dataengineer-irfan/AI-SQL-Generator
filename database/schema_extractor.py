from typing import Dict
from typing import List

from database.oracle_connector import OracleConnector


class SchemaExtractor:

    def __init__(self):

        self.connector = OracleConnector()

    def get_tables(self) -> List[str]:

        sql = """
        SELECT owner,
       table_name
FROM all_tables
WHERE owner NOT IN (
'SYS',
'SYSTEM',
'XDB',
'MDSYS',
'CTXSYS',
'ORDSYS',
'DBSNMP',
'OUTLN'
) ORDER BY table_name """

        conn = self.connector.get_connection()

        cursor = conn.cursor()

        try:

            cursor.execute(sql)

            return [
                row[0]
                for row in cursor.fetchall()
            ]

        finally:

            cursor.close()

    def get_columns(self):

        sql = """
        SELECT
            table_name,
            column_name,
            data_type
        FROM user_tab_columns
        ORDER BY table_name
        """

        conn = self.connector.get_connection()

        cursor = conn.cursor()

        try:

            cursor.execute(sql)

            return cursor.fetchall()

        finally:

            cursor.close()

    def get_primary_keys(self):

        sql = """
        SELECT
            cols.table_name,
            cols.column_name
        FROM all_constraints cons
        JOIN all_cons_columns cols
        ON cons.constraint_name = cols.constraint_name
        WHERE cons.constraint_type='P'
        """

        conn = self.connector.get_connection()

        cursor = conn.cursor()

        try:

            cursor.execute(sql)

            return cursor.fetchall()

        finally:

            cursor.close()

    def get_foreign_keys(self):

        sql = """
        SELECT
            a.table_name,
            a.column_name,
            c_pk.table_name
        FROM all_cons_columns a
        JOIN all_constraints c
            ON a.constraint_name=c.constraint_name
        JOIN all_constraints c_pk
            ON c.r_constraint_name=c_pk.constraint_name
        WHERE c.constraint_type='R'
        """

        conn = self.connector.get_connection()

        cursor = conn.cursor()

        try:

            cursor.execute(sql)

            return cursor.fetchall()

        finally:

            cursor.close()

    def extract_schema(self) -> Dict:

        schema = {}

        columns = self.get_columns()

        for table_name, column_name, data_type in columns:

            if table_name not in schema:

                schema[table_name] = {
                    "columns": []
                }

            schema[table_name]["columns"].append(
                {
                    "column_name": column_name,
                    "data_type": data_type
                }
            )

        return schema
