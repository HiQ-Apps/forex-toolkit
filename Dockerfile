FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY server/requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY server/ .

ENV FLASK_APP=server.app
ENV PYTHONPATH=/app

CMD ["flask", "run", "--host=0.0.0.0"]
