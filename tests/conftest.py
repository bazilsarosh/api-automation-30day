import pytest
from utils import api_client

@pytest.fixture
def api():
    return api_client
