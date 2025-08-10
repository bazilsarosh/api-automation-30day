def test_get_posts(api):
    res = api.get("posts")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list) and len(data) > 0
    sample = data[0]
    # Basic schema-ish checks
    for key in ("userId", "id", "title", "body"):
        assert key in sample
