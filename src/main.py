from enum import Enum

from fastapi import FastAPI, Request, Form 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from pydantic import BaseModel, UUID4
import uuid

import uvicorn

import database

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class ItemStatus(Enum):
    OPEN='open'
    INPROGRESS='in progress'
    FINISHED='finished'

class TodoItem(BaseModel):
    itemId: UUID4
    description:str
    status: ItemStatus
    
class TodoItemList(list):
    def append(self, item):
        if not isinstance(item, TodoItem):
            raise TypeError("Only ToDoItem instances can be added to the list")
        super().append(item)
    def remove(self, item):
        for myitem in self[:]:
            if str(myitem.itemId) == item or myitem.itemId == uuid.UUID(item):
                print("Deleting:", item)
                super().remove(myitem)
            
items = TodoItemList()

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/save", response_class=HTMLResponse)
async def save_list(request: Request, item:Annotated[str, Form()]):
    print(item)
    myuuid = uuid.uuid4()
    print('Your UUID is: ' + str(myuuid))
    task=TodoItem(description=item, itemId=str(myuuid), status=ItemStatus.OPEN) 
    items.append(task)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/delete", response_class=HTMLResponse)
async def delete_route(request: Request, itemId:Annotated[str, Form()]):
    print("Deleting item:", itemId)
    items.remove(itemId)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/start", response_class=HTMLResponse)
async def start_route(request: Request,itemId:Annotated[str, Form()]):
    for item in items:
        if str(item.itemId) == itemId:
            if item.status == ItemStatus.OPEN:
                 item.status = ItemStatus.INPROGRESS
            break 
    print("Starting item:", itemId)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/finish", response_class=HTMLResponse)
async def finish_route(request: Request,itemId:Annotated[str, Form()]):
    for item in items:
        if str(item.itemId) == itemId:
            if item.status == ItemStatus.INPROGRESS:
                 item.status = ItemStatus.FINISHED
            break 
    print("Finishing item:", itemId)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})


@app.get("/", response_class=HTMLResponse)
async def root_route(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

def start_server():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)

if __name__ == "__main__":
    start_server()

