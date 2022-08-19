#!/bin/bash


poetry run gunicorn app:app --workers 2 --worker-class  uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000