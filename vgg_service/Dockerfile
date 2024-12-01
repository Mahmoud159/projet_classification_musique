# Utiliser une image Python de base
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires pour le service VGG19
COPY vgg19_service.py .
COPY models/ ./models
COPY utils.py .
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytest

# Exposer le port de ce service (par ex., 5002)
EXPOSE 5002

# Lancer le service VGG19
CMD ["python", "vgg19_service.py"]
