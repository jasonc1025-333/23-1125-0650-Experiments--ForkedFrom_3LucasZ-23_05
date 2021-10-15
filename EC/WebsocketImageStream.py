import asyncio
import websockets
import sys
import cv2
import base64
import time

class WebsocketServer():
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        #self.FPS = 20
        
    async def handle_connections(self, newWebsocket, path):
        print('new connection:', newWebsocket)
        listen_task = asyncio.ensure_future(self.listen_on(newWebsocket))
        send_task = asyncio.ensure_future(self.send_on(newWebsocket))
        done, pending = await asyncio.wait([listen_task, send_task], return_when=asyncio.FIRST_COMPLETED)
        for task in pending:
            task.cancel()

    async def listen_on(self, websocket):
        print('listener started')
        async for msg in websocket:
            print(msg)

    async def send_on(self, websocket):
        print('sender started')
        currentTime = time.time()
        while True:
            prevTime = currentTime
            currentTime = time.time()
            print("one frame time:", currentTime - prevTime)
            retval, frame = self.camera.read()
            retval, jpg = cv2.imencode('.jpg', frame)
            jpg_as_text = str(base64.b64encode(jpg))[2:-1]
            await websocket.send(jpg_as_text)
            #await asyncio.sleep(1/self.FPS)
            
ws = WebsocketServer()

async def main():
    async with websockets.serve(ws.handle_connections, '', 5000):
        await asyncio.Future() #run forever

if __name__ == '__main__':
    try:
        print("Server begun!")
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit()