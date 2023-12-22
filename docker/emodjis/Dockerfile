FROM python:latest
ARG GITHUB_TOKEN
ARG CORS_ALLOWED_ORIGINS
ARG SERVER_URL
ARG CORS_ALLOWED_ORIGINS
ARG DB_ENGINE
ARG DB_NAME
ARG DB_HOST
ARG DB_USER
ARG DB_PASSWORD
ARG DB_PORT
ENV PYTHONUNBUFFERED 1
WORKDIR /var/apps
COPY manage.py manage.py
COPY config/asgi.py config/asgi.py
COPY config/settings.py config/settings.py
COPY config/urls.py config/urls.py
COPY config/wsgi.py config/wsgi.py
COPY docker-entrypoint.sh docker-entrypoint.sh
RUN pip install emodjis
RUN chmod +x docker-entrypoint.sh
EXPOSE 8000
ENTRYPOINT ["/bin/sh", "docker-entrypoint.sh"]