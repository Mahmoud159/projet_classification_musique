# Utiliser une image Python avec Flask ou tout autre framework web
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers frontend
COPY static/ ./static
COPY templates/ ./templates
COPY app.py .
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port pour le frontend (par ex., 5000)
EXPOSE 5000

# Lancer le frontend
CMD ["python", "app.py"]
