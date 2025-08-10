import pytest
from utils.schema_validator import assert_schema

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

@pytest.mark.smoke
def test_get_first_post(api):
    res = api.get("posts/1")
    assert res.status_code == 200
    data = res.json()
    assert_schema(data, POST_SCHEMA)
