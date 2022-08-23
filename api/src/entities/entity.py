from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from abc import abstractmethod
from uuid import uuid4

db_url = 'localhost:5432'
db_name = 'portfolio'
db_user = 'admin'
db_password = 'admin'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity:
    Id = Column(String, primary_key=True, autoincrement=False)
    CreatedAt = Column(DateTime, nullable=False)
    UpdatedAt = Column(DateTime)
    LastUpdatedBy = Column(String)

    def __init__(self, created_by):
        self.Id = str(uuid4())
        self.CreatedAt = datetime.now()
        self.UpdatedAt = datetime.now()
        self.LastUpdatedBy = created_by

    @abstractmethod
    def json(self):
        pass
