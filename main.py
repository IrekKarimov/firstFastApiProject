from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from models import User

app = FastAPI()


@app.get("/")
async def root():
    data = 'fdfdsfsd'
    return FileResponse("index.html", data)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/calculate")
async def calculate(num1: int = Query(le=5, default=0), num2: int = Query(le=9, default=0)):
    return {"result": num1 + num2}


db1 = [{"id": 1, "username": "Bob", "user_info": "Bob info."}, {"id": 2, "username": "Tom", "user_info": "Tom info."}]

@app.get("/user")
async def get_users():
    return {"message": db1}


@app.get("/user/{id}")
async def get_user(id: int):
    for u in db1:
        if u["id"] == id:
            return {"message": u}
    return {"message": "user not found"}


@app.post("/add_user", response_model=User)
async def add_user(user: User):
    db1.append({"id": user.id, "username": user.username, "user_info": user.user_info})
    return user


