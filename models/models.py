from sqlalchemy import create_engine, Column, Float, String, Integer, Boolean, ForeignKey
from sqlalchemy import declarative_base

# passar o link do db aqui no create_engine
# criar a conexão com o banco de dados
db = create_engine("sqlite:///database/database.db")

# criar a base banco de dados
Base = declarative_base()

# criar as classes/tabelas do banco
# Usuario
# Pedidos
# ItensPedidos


class User(Base):
    __tablename__ = "Users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String, nullable=False)
    password = Column("password", String)
    active = Column("active", Bolean)
    admin = Column("admin", Bolean, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin


# executar a criação dos metadados do seu banco (criar efetivamente)
