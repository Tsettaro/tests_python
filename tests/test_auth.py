from flask import session


def test_auth_login(client):
    responce = client.get("/auth/")
    assert responce.status_code == 200
    responce_text = responce.text
    assert "Log in" in responce_text
    assert "password" in responce_text
    assert "login" in responce_text


def test_auth_login_success(client):
    responce = client.post(
        "/auth/",
        data={"login": "my-login", "password": "my-password"},
        headers={"Content-Type": "multipart/form-data"},
        follow_redirects=True,
    )
    assert responce.status_code == 200
    assert len(responce.history) == 1
    assert responce.history[0].status_code == 302
    assert responce.request.path == "/"


def test_auth_login_session(client):
    with client:
        _ = client.post(
            "/auth/",
            data={"login": "my-login", "password": "my-password"},
            headers={"Content-Type": "multipart/form-data"},
            follow_redirects=True,
        )
        assert "user_id" in session
        assert "role" in session
