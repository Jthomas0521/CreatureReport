import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

FASTAPI_URL = "http://localhost:8000"

st.set_page_config(page_title="Live Scores", layout="wide")
st_autorefresh(interval=60000, key="score-refresh")

st.title("Live NBA Scores")

teams = ["Lakers", "Warriors", "Bulls", "Celtics", "Heat", "Nets", "Knicks"]
selected_teams = st.multiselect("Filter by teams:", teams, default=["Lakers", "Bulls"])

try:
    res = requests.get(f"{FASTAPI_URL}/scores/live")
    if res.status_code == 200:
        games = res.json()
        filtered = [g for g in games if g["team1"] in selected_teams or g["team2"] in selected_teams]
        for game in filtered:
            col1, col2, col3, col4 = st.columns([3, 3, 2, 2])
            col1.markdown(f"**{game['team1']}**")
            col2.markdown(f"vs **{game['team2']}**")
            col3.markdown(f" {game['score']}")
            col4.markdown(f" {game['status']}")
    else:
        st.warning("Could not fetch scores.")
except Exception as e:
    st.error(f"Error: {e}")
