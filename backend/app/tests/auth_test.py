from fastapi.testclient import TestClient
import main
client = TestClient(main.app)

def test_create_basic_user():
    # Register a sample user
    zid = "z5555555"
    password = "secretpassword"

    response = client.post(
        "/auth/register/",
        json={
            "zid": zid,
            "password": password,
            "first_name": "First",
            "last_name": "Last",
            "email": "firstlast@gmail.com",
            "phone": "0444444444",
            "picture": "picture.jpeg",
            "role": 1
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