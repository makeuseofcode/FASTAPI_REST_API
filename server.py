from fastapi import FastAPI
from routes.user_routes import user

app = FastAPI()
app.include_router(user)


@app.get("/")
async def home():
    return {"message": "Hello World"}

