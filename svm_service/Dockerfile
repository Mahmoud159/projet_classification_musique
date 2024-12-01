# Utiliser une image Python de base
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires pour le service SVM
COPY svm_service.py .
COPY models/ ./models
COPY utils.py .
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytest

# Exposer le port de ce service (par ex., 5001)
EXPOSE 5001

# Lancer le service SVM
CMD ["python", "svm_service.py"]
