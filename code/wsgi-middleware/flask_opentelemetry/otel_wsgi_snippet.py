class OpenTelemetryMiddleware:

    def __init__(self, wsgi):
        self.wsgi = wsgi
        # other things

    def __call__(self, environ, start_response):
        try:
            iterable = self.wsgi(environ, start_response)
        except Exception as ex:
            pass
