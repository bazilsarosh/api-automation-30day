import pytest
from utils import api_client

@pytest.fixture
def api():
    # expose our client module so tests can call api.get/post/delete(...)
    return api_client

@pytest.fixture
def user_factory(api):
    # creates users and best-effort cleans them up after the test
    created_ids = []

    def _create(payload: dict):
        res = api.post("users", json=payload)   # our client expects 'json='
        assert res.status_code in (200, 201)
        body = res.json()
        created_ids.append(body.get("id"))
        return body

    yield _create

    for uid in created_ids:
        try:
            api.delete(f"users/{uid}")
        except Exception:
            pass
