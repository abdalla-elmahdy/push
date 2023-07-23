FROM python:3.10.4-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE config.settings.local

WORKDIR /app

COPY ./requirements/ ./requirements
RUN pip install -r ./requirements/local.txt

COPY . .
