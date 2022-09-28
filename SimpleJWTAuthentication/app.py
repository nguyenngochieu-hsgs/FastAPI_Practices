from fastapi import FastAPI
import uvicorn

from routers import posts, users

app = FastAPI()
app.include_router(
    posts.router
)
app.include_router(
    users.router
)

if __name__ == '__main__':
    uvicorn.run("app:app", host="localhost", port=8081, reload=True)
    