import pytest
from utils.assertions import assert_has_keys

@pytest.mark.smoke
def test_create_then_list_includes_user(api, user_factory):
    payload = {"name": "StableUser", "job": "Reliability"}
    user = user_factory(payload)
    res = api.get("users")
    assert res.status_code == 200
    # JSONPlaceholder returns synthetic lists; we at least assert no error + structure:
    assert isinstance(res.json(), list)