from jsonschema import validate, ValidationError

def assert_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise AssertionError(f"Schema validation failed: {e.message}")
