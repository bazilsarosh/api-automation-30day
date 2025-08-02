from utils.api_client import post

def test_create_user():
    payload = {
        "name": "Bazil",
        "job": "QA Engineer"
    }
    response = post("users", payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Bazil"
    print("✅ User created successfully:", data)
