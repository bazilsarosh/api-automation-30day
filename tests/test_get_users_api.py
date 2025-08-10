import pytest
from utils.assertions import assert_has_keys

@pytest.mark.smoke
def test_get_user(api):
    response = api.get("users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    print(f"✅ Retrieved {len(data)} users")