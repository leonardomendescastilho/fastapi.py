from fastapi import APIRouter


order_router = APIRouter(prefix="/order", tags=["order"])


@order_router.get('/')
async def orders():
    '''
    Essa é a rota padrão de pedidos do nosso sistema. Todas as rotas precisam de autentificação para acessar nosso sistema.
    '''
    return {"message": "você acessou a rota de pedidos"}
