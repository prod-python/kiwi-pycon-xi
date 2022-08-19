# Implementing Shared Functionality Using Middleware

This repo contains referenced code and the slides for my [Kiwi Pycon XI talk](https://pretalx.com/kiwipycon-2021/talk/X9R7Q8/).

# Slides

- [PDF](./slides.pdf)
- [PPTX](./slides.pptx)


# Referred Code

## WSGI

- [Django application with framework specific middleware](./code/wsgi-middleware/django_polls)
- [Djang appliction with WSGI middleware ](./code/wsgi-middleware/django_polls_wsgi_wrap/)
- [Django wrapping a Flask application](./code/wsgi-middleware/django_wsgi_flask/)
- [Flask application with framework specific middleware](./code/wsgi-middleware/flask_tutorial/)
- [Flask application with WSGI middleware](./code/wsgi-middleware/flask_opentelemetry/)
- [WSGI application with WSGI middleware](./code/wsgi-middleware/wsgi/)
  
## ASGI

- [ASGI application with ASGI middleware](./code/asgi-middleware/asgi/)
- [FastAPI application with middleware](./code/asgi-middleware/fastapi_hello/)
- [FastAPI application wrapping a WSGI application](./code/asgi-middleware/fastapi_wsgi/)

## gRPC

- [Unary-Unary application](./code/grpc-middleware/unary-unary)
- [Bidirectional streaming](./code/grpc-middleware/bidi-streaming)
  
# Resources to learn more

## Middleware

- http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF 
- https://ironick.typepad.com/ironick/2003/11/the_origin_coin.html
- https://ironick.typepad.com/ironick/2005/07/update_on_the_o.html 
- https://en.wikipedia.org/wiki/Middleware_(distributed_applications) 
- https://dl.acm.org/doi/10.1145/1228291.1228310
- https://queue.acm.org/detail.cfm?id=3526211


## WSGI

- https://web.archive.org/web/20191008011715/https://be.groovie.org/2005/10/07/wsgi_and_wsgi_middleware_is_easy.html
- https://lucumr.pocoo.org/2007/5/21/getting-started-with-wsgi/ 
- https://peps.python.org/pep-0333/

## gRPC intereceptors

- https://github.com/grpc/grpc/tree/master/examples/python/interceptors
- [API documentation for server side intereceptor](https://grpc.github.io/grpc/python/grpc.html#service-side-interceptor)
- [API documentation for client side interceptor](https://grpc.github.io/grpc/python/grpc.html#client-side-interceptor)

