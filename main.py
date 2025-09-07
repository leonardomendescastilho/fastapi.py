from routes.order import order_router
from routes.auth import auth_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)
