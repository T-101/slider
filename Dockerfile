# --- Builder Stage ---
FROM python:3.13.1-alpine3.21 AS builder

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY backend/requirements.txt /app/
RUN apk add --no-cache gcc musl-dev zlib-dev jpeg-dev \
    && pip install uv \
    && uv pip install --prefix=/install -r requirements.txt

# --- Final Stage ---
FROM python:3.13.1-alpine3.21

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=builder /install /usr/local

COPY .bashrc /root/

RUN apk add --no-cache nano bash htop