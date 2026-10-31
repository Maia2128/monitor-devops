from app import app

def test_health():
    cliente = app.test_client()
    resposta = cliente.get("/health")
    assert resposta.status_code == 200
    