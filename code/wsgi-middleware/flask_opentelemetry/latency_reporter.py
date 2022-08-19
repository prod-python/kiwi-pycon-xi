import time


class MyLatencyReporter:

    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):

        request_begin = time.time()
        print("latency_reporter: Calling next view")
        response = self.wsgi_app(environ, start_response)
        print("latency_reporter: back from view")
        print(f"Request took {time.time()-request_begin} seconds")
        return response
