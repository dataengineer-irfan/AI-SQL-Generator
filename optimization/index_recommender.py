import re


class IndexRecommender:

    def recommend(self, sql: str):

        sql_upper = sql.upper()

        recommendations = []
        alias_map = {}

        # FROM CUSTOMERS C
        # JOIN ORDERS O
        # JOIN ORDER_ITEMS OI
        # JOIN PRODUCTS P

        pattern = r"(?:FROM|JOIN)\s+([A-Z_]+)\s+([A-Z_]+)"

        for table_name, alias in re.findall(
            pattern,
            sql_upper
        ):
            alias_map[alias] = table_name

        join_pattern = (
            r"([A-Z_]+)\.([A-Z_]+)\s*=\s*"
            r"([A-Z_]+)\.([A-Z_]+)"
        )

        for (
            left_alias,
            left_column,
            right_alias,
            right_column
        ) in re.findall(
            join_pattern,
            sql_upper
        ):

            left_table = alias_map.get(
                left_alias,
                left_alias
            )

            right_table = alias_map.get(
                right_alias,
                right_alias
            )

            recommendations.append(
                f"CREATE INDEX IDX_{left_table}_{left_column} "
                f"ON {left_table} ({left_column})"
            )

            recommendations.append(
                f"CREATE INDEX IDX_{right_table}_{right_column} "
                f"ON {right_table} ({right_column})"
            )

        unique = []

        seen = set()

        for sql_stmt in recommendations:

            if sql_stmt not in seen:

                seen.add(sql_stmt)

                unique.append(sql_stmt)

        return unique