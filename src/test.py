from app import app

def test_health():
    r = app.test_client().get("/health")   # simula una petición sin levantar servidor
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"