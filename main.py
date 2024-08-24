from fastapi import FastAPI
from . import models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

from .routers import users, products, orders

app.include_router(users.router, prefix="/api")
app.include_router(products.router, prefix="/api")
app.include_router(orders.router, prefix="/api")
