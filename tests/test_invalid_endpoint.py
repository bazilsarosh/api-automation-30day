import pytest
from utils.assertions import assert_has_keys

@pytest.mark.smoke
def test_invalid_endpoint_returns_404(api):
    res = api.get("unknown-endpoint")
    assert res.status_code == 404
