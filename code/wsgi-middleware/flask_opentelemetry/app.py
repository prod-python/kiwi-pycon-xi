from flask import Flask

from latency_reporter import MyLatencyReporter

from opentelemetry.instrumentation.wsgi \
    import OpenTelemetryMiddleware

app = Flask(__name__)
app.wsgi_app = OpenTelemetryMiddleware(app.wsgi_app)
app.wsgi_app = MyLatencyReporter(app.wsgi_app)


@app.route("/")
def hello():
    return "Hello!"


app.run(port=8000)
