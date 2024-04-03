from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

db_url = f"D:/Apps/SQLite/my_db.db"

engine = create_engine(f"sqlite:///{db_url}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

