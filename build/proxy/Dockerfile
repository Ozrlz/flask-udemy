ARG NGINX_VERSION=1.13.10
FROM nginx:${NGINX_VERSION}

ENV HTTP_PORT 5000

RUN apt update && apt install -y nano iputils-ping curl && apt clean

COPY nginx.conf /etc/nginx/conf.d/odoo.conf
COPY ssl /etc/nginx/ssl/

EXPOSE ${HTTP_PORT}