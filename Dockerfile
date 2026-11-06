FROM python:3.11-slim
WORKDIR /finrisk_app
COPY requirements.txt .
COPY ./pip_packages /tmp/pip_packages
RUN pip install --no-cache-dir --no-index --find-links=/tmp/pip_packages -r \
    requirements.txt \
    lightgbm \
    mlflow \
    fastapi \
    uvicorn
    