from fastapi import FastAPI, Depends
from api_pedidos.esquema import Item
from uuid import UUID


app = FastAPI()


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}

@app.get("/orders/{identificacao_do_pedido}/items")
def listar_itens(identificacao_do_pedido: UUID):
    pass


def recuperar_itens_por_pedido(identificacao_do_pedido: UUID) -> list[Item]:
    pass

@app.get("/orders/{identificacao_do_pedido}/items")
def listar_itens(itens: list[Item] = Depends(recuperar_itens_por_pedido)):
    return itens