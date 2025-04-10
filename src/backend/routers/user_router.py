from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.backend.database import SessionLocal
from src.backend.models.user import User

app = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
