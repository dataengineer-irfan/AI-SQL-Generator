from execution.sql_executor import SQLExecutor

sql = """
SELECT *
FROM CUSTOMERS
"""

executor = SQLExecutor()

df = executor.execute(sql)

print(df)
