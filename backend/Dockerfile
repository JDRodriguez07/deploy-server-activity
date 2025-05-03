FROM python:3.9-slim

# Cambiamos el directorio de trabajo al folder backend
WORKDIR /app/backend

# Copiamos primero el requirements.txt para instalar dependencias
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código (asegúrate que el contexto de docker-compose sea el correcto)
COPY . .

# Ejecutamos el servidor usando gunicorn + uvicorn worker
CMD ["gunicorn", "app.main:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
