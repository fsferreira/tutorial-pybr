from fastapi.testclient import TestClient
from http import HTTPStatus


def test_quando_verificar_integridade_devo_ter_como_retorno_codigo_de_status_200():
    cliente = TestClient(app)
    resposta = cliente.get("/healthcheck")
    assert resposta.status_code == HTTPStatus.OK
