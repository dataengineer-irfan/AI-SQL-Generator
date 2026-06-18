import pandas as pd

from dashboard.csv_exporter import (
    CSVExporter
)


df = pd.DataFrame(
    {
        "Country": [
            "USA",
            "France",
            "India"
        ],
        "Sales": [
            12000,
            9000,
            18000
        ]
    }
)

file = CSVExporter.export(
    df
)

print()

print(file)
