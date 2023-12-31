from fastapi import FastAPI, Request, Form 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from pydantic import BaseModel
import logging

import uvicorn

import database

logging.basicConfig(encoding='utf-8', level=logging.CRITICAL)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

items = database.TodoItemList(database.session)

@app.post("/save", response_class=HTMLResponse)
async def save_list(request: Request, item:Annotated[str, Form()]):
    logging.info(item)
    task=database.TodoListItem(description=item, status=database.ItemStatus.OPEN) 
    items.append(task)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/delete", response_class=HTMLResponse)
async def delete_route(request: Request, itemId:Annotated[str, Form()]):
    logging.info("Deleting item: %s", itemId)
    items.remove(itemId)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/start", response_class=HTMLResponse)
async def start_route(request: Request, itemId:Annotated[str, Form()]):
    if items.find_item(itemId):
        items.update_status(itemId)
        logging.info("Starting item: %s", itemId) 
    else:
        logging.alert("Item not found: %s", item.id) 
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/finish", response_class=HTMLResponse)
async def finish_route(request: Request, itemId:Annotated[str, Form()]):
    if items.find_item(itemId):
        items.update_status(itemId)
        logging.info("Finishing item: %s", itemId)
    else:
        logging.alert("Item not found: %s", itemId)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})


@app.get("/", response_class=HTMLResponse)
async def root_route(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

# FIXME use dotenv for port / log level
def start_server():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)

if __name__ == "__main__":
    start_server()

