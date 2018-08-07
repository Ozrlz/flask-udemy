ARG NGINX_VERSION=1.13.10
FROM nginx:${NGINX_VERSION}

ENV HTTP_PORT 5000
ENV HTTPS_PORT 5002

RUN apt update && apt install -y nano iputils-ping curl && apt clean

COPY nginx.conf /etc/nginx/conf.d/odoo.conf
COPY ssl /etc/nginx/ssl/

EXPOSE ${HTTP_PORT} ${HTTPS_PORT}