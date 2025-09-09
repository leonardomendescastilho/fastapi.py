from fastapi import APIRouter, Depends
from models.dependencies import get_session
from models.models import User
from utils import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post('/create_account')
async def create_account(name: str, email: str, password: str, session=Depends(get_session)):
    '''
    Função para criar um novo usuário, caso ele não existir.
    '''
    user = session.query(User).filter(User.email == email).all()

    # validação para ver se o usuario existe
    if user:
        return {"message": "Usuário já está cadastrado"}
    else:
        password_crypt = bcrypt_context.hash(password)
        new_user = User(name, email, password_crypt)
        session.add(new_user)
        session.commit()
        return {"message": "Usuário cadastrado com sucesso"}
