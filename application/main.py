from fastapi import FastAPI
from db import session
from models import UserTable, User

app = FastAPI()

@app.get("/backend/hello")
def root_response():
    return "hello"


@app.get("/backend/users/{user_id}")
def get_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    return user

@app.post("/backend/users")
async def create_user(name: str, keyword: str):
    user = UserTable()
    user.name = name
    user.keyword = keyword
    session.add(user)
    session.commit()