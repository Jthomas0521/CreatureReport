import requests
import os
from dotenv import load_dotenv

load_dotenv()

SPORTSFEED_API_KEY = os.getenv("SPORTSFEED_API_KEY")


def get_live_nba_scores():
    # url = "https://api.mysportsfeed.com/v2.1/pull/nba/current/games.json"
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
    headers = {
        "Authorization": SPORTSFEED_API_KEY
    }

    params = {
        "status": "inprogress"
    }

    response = requests.get(url, headers=headers, params=params, timeout=10)

    if response.status_code == 200:
        games = response.json().get("games", [])
        simplified = []

        for game in games:
            home = game["schedule"]["homeTeam"]["abbreviation"]
            away = game["schedule"]["awayTeam"]["abbreviation"]
            score = f"{game['score']['awayScore']} - {game['score']['homeScore']}"
            status = game["schedule"]["status"]
            simplified.append({
                "home": home,
                "away": away,
                "score": score,
                "status": status
            })
        return simplified
    else:
        raise Exception("Failed to fetch live scores.")
