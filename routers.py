import asyncio
from fastapi import APIRouter
import threading
import time
from robot import async_robot

robot_router = APIRouter(
    prefix="/robot",
    tags=["Robot"],
)

thread_stop = False


@robot_router.post("/start/{start_id}")
def start_robot(start_id: int) -> None:
    asyncio.run(async_robot.start(start_id))


@robot_router.post("/stop")
def stop_robot() -> None:
    asyncio.run(async_robot.stop())


if __name__ == "__main__":
    start_robot(3)
    stop_robot()
    # task = asyncio.create_task(start_loop(start_id))
