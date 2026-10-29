# Imagen base ligera con Python
FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia primero solo las dependencias (aprovecha la caché de capas)
COPY requirements.txt .

# Instala dependencias; --no-cache-dir reduce el tamaño
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Crea un usuario sin privilegios
RUN useradd -m appuser

# El proceso NO corre como root
USER appuser

# Documenta el puerto (no lo publica)
EXPOSE 5000

# Servidor de producción: módulo app, objeto app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]