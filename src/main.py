from fastapi import FastAPI, Request, Form 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from pydantic import BaseModel

import uvicorn

import database

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class TodoItemList(list):
    def __init__(self, session):
        self.session = session
        self.load_initial_data()

    def load_initial_data(self):
        """Load initial data from the database to sync with the list."""
        items = self.session.query(database.TodoListItem).all()
        super().extend(items)

    def append(self, item):
        if not isinstance(item, database.TodoListItem):
            raise TypeError("Only TodoItem instances can be added to the list")
        self.session.add(item)
        try:
            self.session.commit()
            super().append(item)
        except Exception as e:
            self.session.rollback()
            raise e

    def remove(self, item):
        print("Removing:", item)
        to_remove = None
        for myitem in self[:]:
            print("Current item is ", myitem.id)
            if str(myitem.id) == item:
                to_remove = myitem
                break
        if to_remove:
            self.session.delete(to_remove)
            try:
                self.session.commit()
                super().remove(to_remove)
            except Exception as e:
                self.session.rollback()
                raise e
        else:
            raise ValueError("Item not found in the list")


items = TodoItemList(database.session)

@app.post("/save", response_class=HTMLResponse)
async def save_list(request: Request, item:Annotated[str, Form()]):
    print(item)
    task=database.TodoListItem(description=item, status=database.ItemStatus.OPEN) 
    items.append(task)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/delete", response_class=HTMLResponse)
async def delete_route(request: Request, itemId:Annotated[str, Form()]):
    print("Deleting item:", itemId)
    items.remove(itemId)
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/start", response_class=HTMLResponse)
async def start_route(request: Request, itemId:Annotated[str, Form()]):
    for item in items:
        print("Prüfe item.id", item.id)
        print("Teste itemId", itemId)
        if str(item.id) == itemId:
            print("itemId ist", itemId)
            if item.status == database.ItemStatus.OPEN:
                 item.status = database.ItemStatus.INPROGRESS
                 print (itemId)
            break 
    print("Starting item:", itemId) 
    return templates.TemplateResponse("index.html", {"request": request, "items":items})

@app.post("/finish", response_class=HTMLResponse)
async def finish_route(request: Request, itemId:Annotated[str, Form()]):
    for item in items:
        if str(item.id) == itemId:
            if item.status == database.ItemStatus.INPROGRESS:
                 item.status = database.ItemStatus.FINISHED
                 print(itemId)
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

