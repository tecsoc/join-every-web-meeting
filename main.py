import subprocess

from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

app = FastAPI()


class OpenUrlPayload(BaseModel):
    url: str = "https://github.com/tecsoc"


@app.get("/")
def top():
    return PlainTextResponse(content="Hello World!")


@app.get("/api")
def api_top():
    return {"message": "Hello World!"}


@app.post("/api/open-url")
def open_url(payload: OpenUrlPayload, response: Response):
    try:
        subprocess.run(["open", payload.url])
        response.status_code = 200
    except:
        response.status_code = 500

    return {}
