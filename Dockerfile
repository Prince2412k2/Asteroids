FROM jlesage/baseimage-gui:alpine-3.15-v4
WORKDIR /app

COPY . .

RUN apk update && apk add py-pip && apk add python3

RUN pip install pygame

RUN chmod +x /app/startapp.sh

RUN set-cont-env APP_NAME "Asteroid"

