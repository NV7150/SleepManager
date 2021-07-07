from fastapi import FastAPI, HTTPException
from db import session
from models import UserTable, User
from pydantic import BaseModel
import json

class UpdateUser(BaseModel):
    date: str
    wake: str
    sleep: str
    condition: int
    sleep_level: int

class CreateUser(BaseModel):
    name: str
    password: str

app = FastAPI()

@app.get("/backend/users/{user_id}")
def get_user(user_id: int, password: str):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404)

    if not user.password == password:
        raise HTTPException(status_code=403)

    return user

@app.get("/backend/user_id/{user_name}")
def get_id(user_name: str):
    user = session.query(UserTable).filter(UserTable.name == user_name).first()
    if user:
        return user.id
    else:
        raise HTTPException(status_code=404)

@app.post("/backend/users/{user_id}")
async def update_user(user_id: int, password: str, data: UpdateUser):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404)
    if not user.password == password:
        raise HTTPException(status_code=403)

    dates = json.loads(user.data_json)
    dates.append(data.dict())

    user.data_json = json.dumps(dates)
    session.commit()

@app.post("/backend/users")
async def create_user(data: CreateUser):
    new_user = UserTable()
    new_user.name = data.name
    new_user.password = data.password
    session.add(new_user)
    session.commit()

