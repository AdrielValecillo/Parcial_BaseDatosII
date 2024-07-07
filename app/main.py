from fastapi import FastAPI
from app.db.database import engine
import app.db.models as db_models
from app.api.endpoints.comercios import comercio_router
from app.api.schemas import schemas_comercios as schemas
from app.services.comercios_services import ComercioServices

crud = ComercioServices()

app = FastAPI()

db_models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(comercio_router)


