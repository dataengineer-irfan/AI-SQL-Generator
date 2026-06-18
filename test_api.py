import requests

response = requests.post(
    "http://127.0.0.1:8000/generate",
    json={
        "question": "Show total sales by country"
    }
)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)