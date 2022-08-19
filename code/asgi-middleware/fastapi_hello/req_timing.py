import time
from starlette.types import ASGIApp, Receive, Scope, Send


class RequestTimer:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        print(f"{scope['type']}:{scope['path']}: Got request.")
        t1 = time.time()
        await self.app(scope, receive, send)
        print(
            f"{scope['type']}: {scope['path']}: Finished request. {time.time()-t1}s.")
