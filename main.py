from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from models import User

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("index.html")


@app.get("/login")
async def user_login():
    message = 'User sign-in'
    return {"message": message}


@app.get("/logout")
async def user_logout():
    message = 'User logout'
    return {"message": message}


@app.get("/user/profile")
async def user_profile():
    message = 'User profile'
    return {"message": message}


@app.get("/user/update")
async def user_update():
    message = 'User updated'
    return {"message": message}

