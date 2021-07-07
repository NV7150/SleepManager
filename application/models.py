from sqlalchemy import Column,Integer, String
from pydantic import BaseModel
from db import Base, ENGINE

class UserTable(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    data_json = Column(String(16384), nullable=True)

class User(BaseModel):
    id: int
    name: str
    password: str
    data_json: str

def main():
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main()