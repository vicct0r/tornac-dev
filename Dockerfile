
FROM python:3.13-bookworm
 
RUN mkdir /app
 
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 

RUN pip install --upgrade pip 
 
COPY requirements.txt  /app/
COPY entrypoint.sh /entrypoint.sh

RUN pip install --no-cache-dir -r docker.txt
 
COPY . /app/
 
EXPOSE 8001

RUN apt-get update && apt-get install -y netcat-openbsd
ENTRYPOINT [ "/entrypoint.sh" ]