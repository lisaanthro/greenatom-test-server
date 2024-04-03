from sqlalchemy import Integer, DateTime, Interval
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class BaseSqlModel(DeclarativeBase):
    pass


class Entry(BaseSqlModel):
    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    start_id: Mapped[int] = mapped_column(Integer, default=0)
    start_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    time_delta: Mapped[Interval] = mapped_column(Interval, nullable=False)


