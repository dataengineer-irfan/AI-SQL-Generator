from pydantic import BaseModel


class SQLResponse(BaseModel):

    question: str

    sql: str

    execution_time: float
