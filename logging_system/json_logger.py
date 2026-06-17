import json
import os
from datetime import datetime


class JSONLogger:

    def __init__(self):

        os.makedirs(
            "logs",
            exist_ok=True
        )

    def log(
        self,
        filename: str,
        payload: dict
    ):

        filepath = (
            f"logs/{filename}.json"
        )

        payload["timestamp"] = (
            datetime.utcnow()
            .isoformat()
        )

        with open(
            filepath,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                json.dumps(payload)
            )

            f.write("\n")
