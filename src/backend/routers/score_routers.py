from fastapi import APIRouter
from src.backend.services.mysportsfeed import get_live_nba_scores

app = APIRouter()


@app.get("/scores/live")
def live_scores():
    return get_live_nba_scores()
