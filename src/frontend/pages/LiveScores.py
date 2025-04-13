import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

FASTAPI_URL = "http://localhost:8000"

st.set_page_config(page_title="Live Scores", layout="wide")
st_autorefresh(interval=60000, key="score-refresh")

st.title("Live NBA Scores")

try:
    res = requests.get(f"{FASTAPI_URL}/scores/live")
    if res.status_code == 200:
        games = res.json()

        # Get unique team names and statuses
        all_teams = sorted(set([g["team1"] for g in games] + [g["team2"] for g in games]))
        all_statuses = sorted(set([g["status"] for g in games]))

        # Filters
        selected_teams = st.multiselect("Filter by teams:", all_teams, default=all_teams)
        selected_statuses = st.multiselect("Filter by game status:", all_statuses, default=all_statuses)

        # Apply filters
        filtered_games = [
            g for g in games
            if (g["team1"] in selected_teams or g["team2"] in selected_teams)
            and g["status"] in selected_statuses
        ]

        # Display games
        if filtered_games:
            for game in filtered_games:
                col1, col2, col3, col4 = st.columns([3, 3, 2, 2])
                col1.markdown(f"**{game['team1']}**")
                col2.markdown(f"vs **{game['team2']}**")
                col3.markdown(f"{game['score']}")
                col4.markdown(f"{game['status']}")
        else:
            st.info("No games match your filters.")

    else:
        st.warning("Could not fetch scores.")
except Exception as e:
    st.error(f"Error: {e}")
