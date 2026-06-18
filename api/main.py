import time

from fastapi import FastAPI

from api.models.request_models import SQLRequest
from api.models.response_models import SQLResponse

from generation.enhanced_sql_generator import (
    EnhancedSQLGenerator
)

app = FastAPI(
    title="AI SQL Generator",
    version="1.0"
)

generator = EnhancedSQLGenerator()


@app.get("/")
def home():

    return {
        "message": "AI SQL Generator API"
    }


@app.post(
    "/generate",
    response_model=SQLResponse
)
def generate_sql(request: SQLRequest):

    start = time.time()

    sql = generator.generate(
        request.question,
        ""
    )

    elapsed = round(
        time.time() - start,
        3
    )

    return SQLResponse(
        question=request.question,
        sql=sql,
        execution_time=elapsed
    )