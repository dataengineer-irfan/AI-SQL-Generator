import pandas as pd

from dashboard.chart_generator import (
    ChartGenerator
)

df = pd.DataFrame(
    {
        "Country": [
            "USA",
            "France",
            "India",
            "Germany"
        ],
        "Sales": [
            12000,
            9000,
            18000,
            7000
        ]
    }
)

bar = ChartGenerator.bar(
    df,
    "Country",
    "Sales",
    "Sales by Country"
)

line = ChartGenerator.line(
    df,
    "Country",
    "Sales",
    "Sales Trend"
)

pie = ChartGenerator.pie(
    df,
    "Country",
    "Sales",
    "Sales Distribution"
)

print()

print(type(bar))

print(type(line))

print(type(pie))
