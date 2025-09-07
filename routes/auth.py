from fastapi import APIRouter


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get('/')
async def authentication():
    '''
    Essa é a rota padrão de autentificação.
    '''
    return {"message": "Você acessou a rota de autentificação", "auth": False}
