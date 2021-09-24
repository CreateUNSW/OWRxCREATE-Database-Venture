import main

from fastapi.testclient import TestClient
client = TestClient(main.app)

def test_create_basic_user():
    response = client.post(
        "/auth/person/",
        json={
            "zid": "z5555555",
            "password": "secretpassword",
            "first_name": "First",
            "last_name": "Last",
            "email": "firstlast@gmail.com",
            "phone": "0444444444",
            "picture": "picture.jpeg",
            "role": "admin"
        }
    )

    assert response.status_code == 200

    assert response.json() == {
        "zid": "z5555555",
        "first_name": "First",
        "last_name": "Last",
        "email": "firstlast@gmail.com",
        "phone": "0444444444",
        "picture": "picture.jpeg",
    }