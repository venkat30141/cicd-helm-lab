from app import app


def test_home():
    r = app.test_client().get("/")
    assert r.status_code == 200
    assert "message" in r.get_json()


def test_health():
    r = app.test_client().get("/healthz")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}