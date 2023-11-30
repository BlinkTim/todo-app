import enum

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

