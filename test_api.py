import requests

response = requests.post(
    "http://127.0.0.1:8000/generate",
    json={
        "question": "Show total sales by country"
    }
)

print(response.json())
