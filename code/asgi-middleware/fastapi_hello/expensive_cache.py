import base64
from typing import List
from starlette.types import ASGIApp, Receive, Scope, Send
import asyncio
import base64

my_cache = dict()
lock = asyncio.Lock()


async def lookup_result(cache_key: str):
    async with lock:
        return my_cache.get(cache_key)


async def get_cache_key(path, query_string):
    key = path + query_string.decode()
    return base64.b64encode(key.encode("utf-8")).decode()


class ExpensiveCache:
    def __init__(self, app: ASGIApp, excluded_paths: List) -> None:
        self.app = app
        self.excluded_paths = excluded_paths

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or scope['path'] in self.excluded_paths:
            await self.app(scope, receive, send)
            return

        http_method = scope['method']

        if http_method != "GET":
            await self.app(scope, receive, send)
            return

        cache_key = await get_cache_key(scope['path'], scope['query_string'])

        async def cache_and_send(data: dict):
            if http_method == 'GET' and data.get('body'):
                async with lock:
                    my_cache[cache_key] = data.get('body')
            await send(data)

        cached_response = await lookup_result(cache_key)
        if cached_response:
            await send({
                'type': 'http.response.start',
                'status': 200,
                'headers': [
                        [b'content-type', b'application/json'],
                        [b'x-cached-data', b'yes']
                ],
            })
            await send({
                'type': 'http.response.body',
                'body': cached_response,
            })
            return
        await self.app(scope, receive, cache_and_send)
