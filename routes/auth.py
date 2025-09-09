from fastapi import APIRouter, Depends, HTTPException
from models.dependencies import get_session
from models.models import User
from utils import bcrypt_context
from schemas.schemas import UserSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post('/create_account')
async def create_account(user_schema: UserSchema, session: Session = Depends(get_session)):
    '''
    Função para criar um novo usuário, caso ele não existir.
    '''
    user = session.query(User).filter(User.email == user_schema.email).all()

    # validação para ver se o usuario existe
    if user:
        raise HTTPException(
            detail="O usuário já está cadastrado", status_code=400)
    else:
        password_crypt = bcrypt_context.hash(user_schema.password)
        new_user = User(user_schema.name, user_schema.email,
                        password_crypt, user_schema.active, user_schema.admin)
        session.add(new_user)
        session.commit()
        return {"message": f"Usuário cadastrado com sucesso {user_schema.email}"}
