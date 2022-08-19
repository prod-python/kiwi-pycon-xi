import time
import flask_app


class FlaskAppWrapper(object):
    def __init__(self, app):
        self.wsgi_app = app
        self.start_response = None

    def my_start_response(self, status, headers):
        self.status = status
        if not self.status.startswith('404'):
            self.start_response(status, headers)
            return

    def __call__(self, environ, start_response):
        self.start_response = start_response
        data = flask_app.app.wsgi_app(environ, self.my_start_response)
        if not self.status.startswith('404'):
            return data
        print('Got 404')
        return self.wsgi_app(environ, start_response)
