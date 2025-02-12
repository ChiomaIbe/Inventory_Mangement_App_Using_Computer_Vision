from fastapi.reponses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from flaskwebgui import FlaskUI, close_application
from websockets.exceptions import ConnectionClosed
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import cv2, asyncio
from ultralytics import YOLO

app = FastAPI()
camera = cv2.VideoCapture(0)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/close")
async def close_server():
    close_application()

def start_fastapi(**kwargs):
    import uvicorn
    uvicorn.run(**kwargs)

@app.websockets("/ws")
async def get_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                model = YOLO("yolov5s.pt")
                results = model.predict(frame, device=[0])
                frame = result[0].plot()
                ret, buffer = cv2.imencode('.jpg', frame)
                await websocket.send_bytes(buffer.tobytes())
                await websocket.send_text("some text")
            await asyncio.sleep(0.03)
    except (WebSocketDisconnect, ConnectionClosed):
        print("Client disconnected")

if __name__ == "__main__":

    FlaskUI(
        server="fastapi",
        server_kwargs={
            "app": app,
            "host": "0.0.0.0",
            "port": 8000
        },
        width=800,
        height=600,
    ).run()