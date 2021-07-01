from sqlalchemy import Column,Integer, String
from pydantic import BaseModel
from db import Base, ENGINE

class UserTable(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    keyword = Column(String(30))

class User(BaseModel):
    id: int
    name: str
    keyword: str

def main():
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main()