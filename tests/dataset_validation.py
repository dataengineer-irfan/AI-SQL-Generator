from validation.auto_corrector import AutoCorrector

validator = AutoCorrector()

sql = """
SELECT COUNTRY,
SUM(SALES)
FROM SALES_DATA_SAMPLE
GROUP BY COUNTRY
"""

print(
    validator.validate(sql)
)