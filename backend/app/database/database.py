from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Leer variables de entorno
DB_USERNAME = os.getenv("username")
DB_PASSWORD = os.getenv("password")
DB_DATABASE = os.getenv("database")
DB_HOST = "mysql"  # Este será el nombre del servicio en docker-compose
DB_PORT = "3306"

# Construir la URL de conexión
DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

# Crear el motor
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base declarativa
Base = declarative_base()
