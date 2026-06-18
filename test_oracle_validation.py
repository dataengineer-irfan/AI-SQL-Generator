from validation.auto_corrector import AutoCorrector

validator = AutoCorrector()

sql = """
SELECT *
FROM CUSTOMERS
"""

print(
    validator.validate(sql)
)
