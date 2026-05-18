FROM python:3.13-bookworm

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

RUN chown -R dockeruser:dockermanager /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY --chown=dockeruser:dockermanager . .

EXPOSE 8000

USER dockeruser

ENTRYPOINT ["/entrypoint.sh"]
