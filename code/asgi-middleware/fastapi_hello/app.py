import asyncio

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import random


from expensive_cache import ExpensiveCache
from req_timing import RequestTimer

app = FastAPI()
app.add_middleware(ExpensiveCache, excluded_paths=["/chat"])
app.add_middleware(RequestTimer)


@app.get("/expensive")
async def root():
    await asyncio.sleep(10)
    return {"message": "Expensive calculation completed"}


@app.post("/exception")
async def exception():
    if random.random() > 0.5:
        raise Exception("Oh no!")
    return {'message': 'Exception avoided!'}


@app.middleware("http")
async def exc_handler(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        print("Exception: ", e)
        return HTMLResponse(
            'An error occured!', status_code=500, headers={'x-exception-handled': 'application'}
        )

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/chat")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect as e:
        print("WebSocketDisconnect: ", e)
