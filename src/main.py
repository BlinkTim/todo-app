from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.post("/save", response_class=HTMLResponse)
async def save_list(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/delete", response_class=HTMLResponse)
async def delete_route(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/start", response_class=HTMLResponse)
async def start_route(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/", response_class=HTMLResponse)
async def root_route(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

