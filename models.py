from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    user_info: str
