poetry run gunicorn app:app --workers 1 --worker-class  uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Debugging tips

## lifespan startup error

https://stackoverflow.com/questions/64512286/asgi-lifespan-protocol-appears-unsupported

```
$ poetry run uvicorn app:app --lifespan on

```