from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://todo_user:todo_password@localhost/todos')


Base = declarative_base()

class ItemStatus(Enum):
    OPEN='open'
    INPROGRESS='in progress'
    FINISHED='finished'

class TodoListItems(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    description = Column(String(128))
    status = Column(String(16))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a new todo list item
new_task = TodoListItems(description="buy shoes", status="done")
session.add(new_task)
session.commit()

# Query tasks
tasks = session.query(TodoListItems).all()
for task in tasks:
        print(task.description)

session.close()
