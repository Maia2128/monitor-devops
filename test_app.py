from app import app

def test_health():
    cliente = app.test_client()
    resposta = cliente.get("/health")
    assert resposta.status_code == 200
    assert resposta.get_json()["status"] == "healthy" 

def test_status():
    cliente = app.test_client()
    resposta = cliente.get("/status")
    assert resposta.status_code == 200
    assert resposta.get_json()["status"] == "online"