import requests

question = "Top 10 customers by sales"

response = requests.post(
    "http://127.0.0.1:8000/generate",
    json={
        "question": question
    }
)

print(response.json())
