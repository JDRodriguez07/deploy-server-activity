# Import FastAPI to create the application
from fastapi import FastAPI

# Import the database engine and Base class to manage tables
from app.database.database import engine, Base

# Later, your routers will be imported here
# from routers.legend_router import router as legend_router
# from routers.legend_type_router import router as legend_type_router

# Create a FastAPI app instance
app = FastAPI(
    title="FastAPI Example",
    root_path="/api",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "persistAuthorization": True,
    },
)

# Create the database tables automatically at startup
Base.metadata.create_all(bind=engine)

# Routers (endpoints) will be included here later
# app.include_router(legend_router, prefix="/legends", tags=["Legends"])
# app.include_router(legend_type_router, prefix="/legend-types", tags=["Legend Types"])

# Basic root route to check if the API is working
@app.get("/get")
def read_root():
    return {"message": "Welcome to Apex Legends API!"}

