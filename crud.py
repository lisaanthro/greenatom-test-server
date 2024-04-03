from typing import Type
import datetime
from sqlalchemy.orm import Session

import models
from models import Entry


def add_entry(db: Session, start_id: int, start_time: datetime.datetime) -> None:
    end_time: datetime.datetime = datetime.datetime.now()
    time_delta: datetime.timedelta = end_time - start_time

    db.add(Entry(
        start_id=start_id,
        start_time=start_time,
        end_time=end_time,
        time_delta=time_delta,
    ))
    db.commit()


def get_all_entries(db: Session) -> list[Type[Entry]]:
    entries = db.query(models.Entry).all()
    return entries

