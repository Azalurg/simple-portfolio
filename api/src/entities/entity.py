from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'localhost:5432'
db_name = 'portfolio'
db_user = 'admin'
db_password = 'admin'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity:
    Id = Column(Integer, primary_key=True)
    CreatedAt = Column(DateTime, nullable=False)
    UpdatedAt = Column(DateTime)
    LastUpdatedBy = Column(String)

    def __init__(self, created_by):
        self.CreatedAt = datetime.now()
        self.UpdatedAt = datetime.now()
        self.LastUpdatedBy = created_by
