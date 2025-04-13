import requests


def get_live_nba_scores():
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        events = data.get("events", [])
        simplified = []

        for event in events:
            competition = event["competitions"][0]
            competitors = competition["competitors"]
            team1 = competitors[0]["team"]["displayName"]
            team2 = competitors[1]["team"]["displayName"]
            score1 = competitors[0]["score"]
            score2 = competitors[1]["score"]
            status = competition["status"]["type"]["description"]

            simplified.append({
                "team1": team1,
                "team2": team2,
                "score": f"{score1} - {score2}",
                "status": status
            })

        return simplified
    except Exception as e:
        print(f"Error fetching live scores: {e}")
        raise Exception("Failed to fetch live scores.")
