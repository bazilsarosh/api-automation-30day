def assert_has_keys(obj, keys):
    missing = [k for k in keys if k not in obj]
    if missing:
        raise AssertionError(f"Missing keys: {missing}")