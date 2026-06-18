import json
import os
from datetime import datetime


class HistoryManager:

    def __init__(
        self,
        history_file="query_history.json"
    ):

        self.history_file = history_file

        if not os.path.exists(
            self.history_file
        ):

            with open(
                self.history_file,
                "w"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )

    def save(
        self,
        question,
        sql,
        execution_time
    ):

        history = self.load()

        history.append(

            {

                "timestamp": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                "question": question,

                "sql": sql,

                "execution_time": execution_time

            }

        )

        with open(
            self.history_file,
            "w"
        ) as file:

            json.dump(
                history,
                file,
                indent=4
            )

    def load(self):

        with open(
            self.history_file,
            "r"
        ) as file:

            return json.load(file)

    def clear(self):

        with open(
            self.history_file,
            "w"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )
