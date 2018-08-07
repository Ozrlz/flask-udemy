# Place here your cert and key

Place here your cert and key as cert.crt and key.key.

You can generate your self-signed crtificates with openssl:

> * openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365