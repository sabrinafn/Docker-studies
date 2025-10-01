# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim

# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Avoid file permission errors with matplotlib
ENV MPLCONFIGDIR=/tmp/.matplotlib
RUN mkdir -p /tmp/.matplotlib

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY app/ ./app
COPY .streamlit ./app/.streamlit

EXPOSE 8001

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8001"]
