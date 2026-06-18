import pandas as pd


class CSVExporter:

    @staticmethod
    def export(
        dataframe,
        filename="results.csv"
    ):

        dataframe.to_csv(
            filename,
            index=False
        )

        return filename
