from fastapi import FastAPI, Request, Form 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.post("/save", response_class=HTMLResponse)
async def save_list(request: Request, item:Annotated[str, Form()]):
    print(item)
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/delete", response_class=HTMLResponse)
async def delete_route(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/start", response_class=HTMLResponse)
async def start_route(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/", response_class=HTMLResponse)
async def root_route(request: Request):
    items = [1,2,3,4,5,6]
    return templates.TemplateResponse("index.html", {"request": request, "items":items})


