import enum

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import logging

# FIXME: use dotenv here
engine = create_engine('mysql+mysqlconnector://todo_user:todo_password@localhost/todos')

Base = declarative_base()

class ItemStatus(enum.Enum):
    OPEN='open'
    INPROGRESS='in progress'
    FINISHED='finished'

class TodoListItem(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(128))
    status = Column(Enum(ItemStatus))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class TodoItemList(list):
    def __init__(self, session):
        self.session = session
        self.load_initial_data()

    def load_initial_data(self):
        """Load initial data from the database to sync with the list."""
        items = self.session.query(TodoListItem).all()
        super().extend(items)

    def find_item(self, itemId):
        for item in self[:]:
            logging.info("Prüfe item.id %s", item.id)
            logging.info("Teste itemId %s", itemId)
            if str(item.id) == itemId:
                logging.info("itemId ist %s", itemId)
                return item
        return None
 
    def update_status(self, item):
        itemObject = self.find_item(item)
        if itemObject == None:
            return None

        logging.info("Changing item status from:%s",itemObject.status)
        # TODO: use match here
        if itemObject.status == ItemStatus.OPEN:
            itemObject.status = ItemStatus.INPROGRESS
        elif itemObject.status == ItemStatus.INPROGRESS:
            itemObject.status = ItemStatus.FINISHED
 
        self.session.commit()
        logging.info("Changed item status to: %s", itemObject.status)


    def append(self, item):
        if not isinstance(item, TodoListItem):
            raise TypeError("Only TodoItem instances can be added to the list")
        self.session.add(item)
        try:
            self.session.commit()
            super().append(item)
        except Exception as e:
            self.session.rollback()
            raise e

    def remove(self, item):
        logging.info("Removing:", item)
        to_remove = None
        for myitem in self[:]: # FIXME: use find_item here
            logging.info("Current item is ", myitem.id)
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


