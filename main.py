from fastapi import FastAPI
import uvicorn

from routers import robot_router
from db import engine
from models import BaseSqlModel


def create_tables() -> None:
    BaseSqlModel.metadata.create_all(bind=engine)


app = FastAPI(title="Robot server")
app.include_router(robot_router)


if __name__ == "__main__":
    create_tables()
    uvicorn.run("main:app", reload=True)
