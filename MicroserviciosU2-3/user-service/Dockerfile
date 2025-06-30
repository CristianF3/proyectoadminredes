#Imagen base ligera de Python
FROM python:3.11-slim

#Directorio de trabajo en el contenedor
WORKDIR /app
#Copia e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y curl

#Copia el código de la app
COPY ./app ./app

#Comando para arrancar el servidor con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
