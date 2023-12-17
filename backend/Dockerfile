FROM python:3.12.1-alpine3.19

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN apk update \
    && apk add gcc python3-dev musl-dev \
    && apk add nano bash htop \
    && apk add zlib-dev jpeg-dev

# to change this default, build using --build-arg timezone=Something/Else
ARG timezone=Europe/Helsinki
ENV TZ=${timezone}

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY .bashrc /root/
