from ..main import app
from fastapi.testclient import TestClient
client = TestClient(app)

import json

def test_create_basic_user():
    response = client.post(
        "/auth/person",
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

    assert response.json() == {
        "zid": "z5555555",
        "password": "secretpassword",
        "first_name": "First",
        "last_name": "Last",
        "email": "firstlast@gmail.com",
        "phone": "0444444444",
        "picture": "picture.jpeg",
        "role": "admin"
    }