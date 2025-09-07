from sqlalchemy import create_engine, Column, Float, String, Integer, Boolean, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy import declarative_base

# passar o link do db aqui no create_engine
# criar a conexão com o banco de dados
db = create_engine("sqlite:///database/database.db")

# criar a base banco de dados
Base = declarative_base()

# criar as classes/tabelas do banco


class User(Base):
    __tablename__ = "users"

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


class Order(Base):
    __tablename__ = "orders"

    ORDER_STATUS = (
        ("PENDING", "PENDING"),
        ("CANCELED", "CANCELED"),
        ("FINALIZED", "FINALIZED")
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user = Column("user", ForeignKey("Users.id"))
    status = Column("status", ChoiceType(
        choices=ORDER_STATUS))
    total_price = Column("total_price", Float)
    # items = Column()

    def __init__(self, user, status="PENDING", total_price=0):
        self.user = user
        self.status = status
        self.total_price = total_price


class OrderItems(Base):
    __tablename__ = "orders_items"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    order = Column("order", ForeignKey("orders.id"))
    quantity = Column("quantity", Integer)
    flavor = Column("flavor", String)
    size = Column("size", String)
    unit_price = Column("unit_price", Float)

    def __init__(self, order, quantity, flavor, size, unit_price):
        self.order = order
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unit_price = unit_price

    # executar a criação dos metadados do seu banco (criar efetivamente)
