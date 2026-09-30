from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="ComicCraft")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


class ComicRequest(BaseModel):
    prompt: str


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/generate")
async def generate_comic(data: ComicRequest):
    prompt = data.prompt.strip()

    panels = [
        f"Panel 1: The story begins with {prompt}.",
        "Panel 2: The main character discovers something unexpected.",
        "Panel 3: A new challenge appears.",
        "Panel 4: The character decides to face the challenge.",
        "Panel 5: An exciting moment changes everything.",
        "Panel 6: The adventure reaches a memorable ending."
    ]

    return {
        "title": "ComicCraft Story",
        "panels": panels
    }