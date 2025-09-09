from sqlalchemy.orm import sessionmaker
from models.models import db


def get_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        # retorna a variável da sessão sem fechar com o 'return' classico
        yield session
    finally:
        session.close()
