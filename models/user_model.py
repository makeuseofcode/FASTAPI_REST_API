from pydantic import BaseModel 

class User(BaseModel):
    name: str
    role: str