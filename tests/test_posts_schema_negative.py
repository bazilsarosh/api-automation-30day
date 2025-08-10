import pytest
from utils.schema_validator import assert_schema

BAD_SCHEMA = {
    "type": "object",
    "properties": {"title": {"type": "integer"}},  # wrong on purpose
    "required": ["title"]
}

def test_post_schema_negative(api):
    res = api.get("posts/1")
    assert res.status_code == 200
    with pytest.raises(AssertionError):
        assert_schema(res.json(), BAD_SCHEMA)
