from fastapi import FastAPI
from api.endpoints import users

app = FastAPI()

#Routers
app.include_router(users.users_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
