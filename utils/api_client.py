import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get(endpoint):
    return requests.get(f"{BASE_URL}/{endpoint}")

def post(endpoint, payload):
    return requests.post(f"{BASE_URL}/{endpoint}", json=payload)

def delete(endpoint):
    return requests.delete(f"{BASE_URL}/{endpoint}")