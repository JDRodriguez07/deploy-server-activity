from fastapi import FastAPI
from app.database.database import engine, Base


# Aquí luego importaremos tus routers
# from routers.legend_router import router as legend_router
# from routers.legend_type_router import router as legend_type_router

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir las rutas aquí
# app.include_router(legend_router, prefix="/legends", tags=["Legends"])
# app.include_router(legend_type_router, prefix="/legend-types", tags=["Legend Types"])

@app.get("/get")
def read_root():
    return {"message": "Welcome to Apex Legends API!"}


