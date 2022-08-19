from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask

flask_app = Flask(__name__)


@flask_app.route("/")
def flask_main():
    return f"Hello world from Flask!"


app = FastAPI()


@app.get("/v2/")
def read_main():
    return {"message": "Hello World from FastAPI"}


app.mount("/v1", WSGIMiddleware(flask_app))
