from fastapi import FastAPI, Depends
from .database import database, create_tables
from fastapi_app import crud
from fastapi_app import schemas

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    create_tables()  

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate):
    user_id = await crud.create_user(user)
    return {"id": user_id, **user.dict()}

@app.get("/users/", response_model=list[schemas.User])
async def read_users():
    return await crud.get_users()