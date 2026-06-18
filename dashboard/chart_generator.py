import plotly.express as px


class ChartGenerator:

    @staticmethod
    def bar(
        dataframe,
        x,
        y,
        title="Bar Chart"
    ):

        return px.bar(
            dataframe,
            x=x,
            y=y,
            title=title
        )

    @staticmethod
    def line(
        dataframe,
        x,
        y,
        title="Line Chart"
    ):

        return px.line(
            dataframe,
            x=x,
            y=y,
            title=title
        )

    @staticmethod
    def pie(
        dataframe,
        names,
        values,
        title="Pie Chart"
    ):

        return px.pie(
            dataframe,
            names=names,
            values=values,
            title=title
        )
