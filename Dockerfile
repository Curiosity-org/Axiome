FROM python:3.11
LABEL maintainer="Aeris One <aeris@aeris-one.fr>"

# Disable python cache files
ENV PYTHONDONTWRITEBYTECODE=1

# Disable buffer output
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y libffi-dev libnacl-dev python3-dev
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Create non-root user to launch the bridge
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

VOLUME ["/app/data"]

CMD ["python", "main.py"]
