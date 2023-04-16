FROM python:3.11
LABEL maintainer="Aeris One <aeris@aeris-one.fr>"

# Empêcher Python de stocker les fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Désactiver le tampon de sortie pour un meilleur logging
ENV PYTHONUNBUFFERED=1

# Installer les dépendances
COPY requirements.txt .
RUN apt-get update && apt-get install -y libffi-dev libnacl-dev python3-dev && python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Créer un utilisateur non-root pour lancer l'application
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

VOLUME ["/app/data"]

CMD ["python", "main.py"]