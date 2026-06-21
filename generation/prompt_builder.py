from typing import List


class PromptBuilder:

    @staticmethod
    def build(
        question: str,
        schema_context
    ) -> str:

        if isinstance(schema_context, list):

            schema_text = "\n\n".join(schema_context)

        else:

            schema_text = str(schema_context)

        return f"""
You are an expert SQL generator.

The SQL will run in DuckDB against ONE CSV dataset.

========================================
DATABASE
========================================

There is ONLY ONE table:

SALES_DATA_SAMPLE

Columns:

ORDERNUMBER
QUANTITYORDERED
PRICEEACH
ORDERLINENUMBER
SALES
ORDERDATE
STATUS
QTR_ID
MONTH_ID
YEAR_ID
PRODUCTLINE
MSRP
PRODUCTCODE
CUSTOMERNAME
PHONE
ADDRESSLINE1
ADDRESSLINE2
CITY
STATE
POSTALCODE
COUNTRY
TERRITORY
CONTACTLASTNAME
CONTACTFIRSTNAME
DEALSIZE

========================================
ADDITIONAL CONTEXT
========================================

{schema_text}

========================================
RULES
========================================

1. Use ONLY the table SALES_DATA_SAMPLE.

2. NEVER reference any other table.

3. NEVER generate JOIN statements.

4. NEVER generate subqueries unless absolutely required.

5. NEVER use Oracle SQL.

6. NEVER use:
   - SYSDATE
   - TRUNC
   - NVL
   - ROWNUM
   - DUAL
   - CONNECT BY

7. Generate DuckDB-compatible SQL.

8. Use only the listed columns.

9. If the user asks for sales by country, use:

SELECT COUNTRY,
       SUM(SALES) AS TOTAL_SALES
FROM SALES_DATA_SAMPLE
GROUP BY COUNTRY

10. Return ONLY SQL.

========================================
QUESTION
========================================

{question}
"""