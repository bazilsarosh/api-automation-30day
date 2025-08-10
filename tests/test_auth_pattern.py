import os
import pytest
from importlib import reload
from utils import api_client as client

@pytest.mark.auth
def test_auth_header_is_attached(monkeypatch):
    monkeypatch.setenv("API_KEY", "demo-token")
    # Force reload headers (simple pattern)
    reload(client)

    r = client.get("posts/1")
    assert r.status_code == 200

    # We can't assert server-side auth on a public API, but we ensure no crash and header present
    hdrs = client._headers()  # accessing internal helper is fine in a learning repo
    assert "Authorization" in hdrs and hdrs["Authorization"].endswith("demo-token")
