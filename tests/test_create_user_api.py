def test_create_user(api):
    payload = {
        "name": "Bazil",
        "job": "QA Engineer"
    }
    response = api.post("users", payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Bazil"
    print("✅ User created successfully:", data)
