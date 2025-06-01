from fastapi import FastAPI
from app import models, database
from app.routers import auth_router, router

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="GEM API",
    description="API do Grupo Economia do Mar",
    version="1.0.0"
)

app.include_router(auth_router.router)
app.include_router(router.router)
