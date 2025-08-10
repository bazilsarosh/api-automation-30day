import pytest

def test_invalid_endpoint_returns_404(api):
    res = api.get("unknown-endpoint")
    assert res.status_code == 404
