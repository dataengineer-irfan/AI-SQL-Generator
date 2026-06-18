from dashboard.history_manager import (
    HistoryManager
)

history = HistoryManager()

history.clear()

history.save(
    question="Sales by Country",
    sql="""
SELECT COUNTRY,
SUM(SALES)
FROM SALES_DATA_SAMPLE
GROUP BY COUNTRY
""",
    execution_time=0.48
)

history.save(
    question="Top Customers",
    sql="""
SELECT CUSTOMERNAME,
SUM(SALES)
FROM SALES_DATA_SAMPLE
GROUP BY CUSTOMERNAME
""",
    execution_time=0.72
)

print()
print(history.load())
