from fastapi import FastAPI
import uvicorn

from routers import robot_router

app = FastAPI(title="Robot server")
app.include_router(robot_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
