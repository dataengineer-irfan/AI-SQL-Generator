from validation.dataset_validator import DatasetValidator

validator = DatasetValidator()

sql = """
SELECT COUNTRY,
SUM(SALES)
FROM SALES_DATA_SAMPLE
GROUP BY COUNTRY
"""

print(
    validator.validate(sql)
)