import random


def simple_handler(environ, start_response):

    if random.random() > 0.5:
        raise Exception('Oh no!')
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    ret = [b'Hello world\n']
    return ret


class MyExceptionProcessor:

    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        try:
            for item in self.wsgi_app(environ, start_response):
                yield item
        except Exception as e:
            print(e)
            status = '500 Something Went Wrong'
            headers = [('X-Error-Processed', 'Handled')]
            start_response(status, headers)
            for item in [b'An error occured!\n']:
                yield item


app = MyExceptionProcessor(simple_handler)
