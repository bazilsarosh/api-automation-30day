import pytest
from utils.data_loader import load_json

# Reuse the 'api' fixture from your conftest.py
testdata = load_json("tests/data/users.json")

@pytest.mark.parametrize("payload", testdata, ids=[f'{d["name"]}-{d["job"]}' for d in testdata])
def test_create_user_data_driven(api, payload):
    res = api.post("users", payload)
    assert res.status_code == 201
    body = res.json()
    # JSONPlaceholder echoes fields back
    for k, v in payload.items():
        assert body.get(k) == v
