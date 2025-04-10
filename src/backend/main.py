from fastapi import FastAPI
from src.backend.routers import user_router, score_routers
from src.backend.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router.app)
app.include_router(score_routers.app)
