import random


async def simple_handler(scope, receive, send):
    request = await receive()

    if random.random() > 0.5:
        raise Exception('Oh no!')
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, ASGI here!',
    })


async def exc_handler(handler, scope, receive, send):
    try:
        await handler(scope, receive, send)
    except Exception as e:
        print("exc_handler:", e)
        await send({
            'type': 'http.response.start',
            'status': 500,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': b'An unexpected error!',
        })


class RateLimiter(object):

    def __init__(self, asgi_app):
        self.asgi_app = asgi_app

    async def __call__(self, scope, receive, send):
        # Needed for uvicorn so that it knows that our app has
        # started correctly
        if scope["type"] == "lifespan":
            msg = await receive()
            if msg["type"] == "lifespan.startup":
                await send(
                    {
                        "type": "lifespan.startup.complete"
                    }
                )
        assert scope["type"] == "http"

        if self.allowed(scope):
            await exc_handler(self.asgi_app, scope, receive, send)
        else:
            await send({
                'type': 'http.response.start',
                'status': 422,
                'headers': [
                        [b'content-type', b'text/plain'],
                ],
            })
            await send({
                'type': 'http.response.body',
                'body': b'Request exceeds limits',
            })

    def allowed(self, scope):
        if random.random() > 0.5:
            return True
        return False


app = RateLimiter(simple_handler)
