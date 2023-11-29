from fastapi import FastAPI, Request, Form 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from pydantic import BaseModel, UUID4
import uuid

app = FastAPI()

templates = Jinja2Templates(directory="templates")


class TodoItem(BaseModel):
    itemId: UUID4
    description:str
    status: str 
    
class TodoItemList(list):
    def append(self, item):
        if not isinstance(item, TodoItem):
            raise TypeError("Only ToDoItem instances can be added to the list")
        super().append(item)
    def remove(self, item):
        for myitem in self[:]:
            if str(myitem.itemId) == item or myitem.itemId == UUID(item):
                print("Deleting:", item)
                super().remove(myitem)
            
items = TodoItemList()

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/save", response_class=HTMLResponse)
async def save_list(request: Request, item:Annotated[str, Form()]):
    print(item)
    myuuid = uuid.uuid4()
    print('Your UUID is: ' + str(myuuid))
    task=TodoItem(description=item, itemId=str(myuuid), status="neu") 
    items.append(task)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/delete", response_class=HTMLResponse)
async def delete_route(request: Request, itemId:Annotated[str, Form()]):
    print("Deleting item:", itemId)
    items.remove(itemId)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/start", response_class=HTMLResponse)
async def start_route(request: Request,itemId:Annotated[str, Form()]):
    print("Starting item:", itemId)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})


@app.get("/", response_class=HTMLResponse)
async def root_route(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items":items})


