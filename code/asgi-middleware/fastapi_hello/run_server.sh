#!/bin/bash


poetry run gunicorn app:app \
    --workers 1 --worker-class  uvicorn.workers.UvicornWorker \
    --bind 127.0.0.1:8000