#!/bin/bash
mkdir -p tls
openssl req -x509 -newkey rsa:4096 -keyout tls/server.key -out tls/server.crt \
    -days 365 \
    -subj "/C=AU/ST=NSW/L=Sydney/O=Echorand/OU=Org/CN=localhost" \
    -extensions san \
    -config <(echo '[req]'; echo 'distinguished_name=req';
            echo '[san]'; echo 'subjectAltName=DNS:user-sessions, DNS:localhost') \
    -nodes
