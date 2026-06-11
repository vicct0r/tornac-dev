FROM python:3.13-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends netcat-openbsd \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd -g 10001 dockermanager && \
    useradd -u 10001 -g dockermanager -m -s /bin/bash dockeruser

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY --chown=dockeruser:dockermanager . .

RUN mkdir -p /app/staticfiles /app/media \
 && chown -R dockeruser:dockermanager /app

EXPOSE 8000

# tirando do rootuser
USER dockeruser
ENTRYPOINT ["/entrypoint.sh"]