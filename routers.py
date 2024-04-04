from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.robot import add_entry, get_all_entries

from robot_script import async_robot

robot_router = APIRouter(
    prefix="/robot",
    tags=["Robot"],
)


@robot_router.post("/start/{start_id}")
async def start_robot(start_id: int) -> dict:
    await async_robot.start(start_id)
    return {"info": "Robot started"}


@robot_router.post("/stop")
async def stop_robot(db: Session = Depends(get_db)) -> dict:
    add_entry(db, async_robot.start_id, async_robot.start_time)
    await async_robot.stop()
    return {"info": "Robot stopped!"}


@robot_router.get("/entries")
def get_entry(db: Session = Depends(get_db)):
    entries = get_all_entries(db)
    return entries

