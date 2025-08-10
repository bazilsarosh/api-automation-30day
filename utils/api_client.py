import os
import requests

def _base_url():
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")

def _headers(extra=None):
    extra = extra or {}
    headers = {"Content-Type": "application/json"}
    api_key = os.getenv("API_KEY", "")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    headers.update(extra)
    return headers

def _url(path):
    return f"{_base_url()}/{path.lstrip('/')}"

def get(path, **kwargs):
    headers = _headers(kwargs.pop("headers", None))
    return requests.get(_url(path), headers=headers, **kwargs)

def post(path, json=None, **kwargs):
    headers = _headers(kwargs.pop("headers", None))
    return requests.post(_url(path), json=json, headers=headers, **kwargs)

def delete(path, **kwargs):
    headers = _headers(kwargs.pop("headers", None))
    return requests.delete(_url(path), headers=headers, **kwargs)
