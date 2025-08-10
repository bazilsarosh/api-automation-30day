from utils.retry import retry

def test_get_posts_resilient(api):
    res = retry(lambda: api.get("posts"), attempts=3, delay=0.5)
    assert res.status_code == 200
