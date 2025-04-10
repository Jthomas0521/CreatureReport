🏀 Creature Report - Live Sports Dashboard

Creature Report is a Bleacher Report-style app for tracking NBA scores, registering users, and filtering team-based content. Built using FastAPI + Streamlit with real-time data from MySportsFeeds.

⚙️ Features
✅ FastAPI backend

✅ Streamlit dashboard (multipage)

✅ Auto-refreshing live NBA scores

✅ Team filter and dark mode toggle

✅ User registration with favorite teams

📁 Project Structure
bash
Copy
Edit
CreatureReport/
├── .env                     # API key (not checked in)
├── .env.example             # Template env file
├── README.md
├── requirements.txt
├── src/
│   └── backend/
│       ├── main.py
│       ├── routers/
│       │   ├── user_routers.py
│       │   └── score_routers.py
│       └── services/
│           └── mysportsfeed.py
├── frontend/
│   ├── Home.py
│   ├── pages/
│   │   ├── LiveScores.py
│   │   └── Users.py
│   └── .streamlit/
│       └── config.toml

🚀 Getting Started
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/Jthomas0521/CreatureReport.git
cd CreatureReport
2. Set up virtual environment
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\activate on Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add your .env
Create a .env file in the root:

env
Copy
Edit
MYSPORTS_API_KEY=Basic your_base64_api_key_here
Or copy the template:

bash
Copy
Edit
cp .env.example .env

🧠 Usage
Start the backend (FastAPI)
bash
Copy
Edit
uvicorn src.backend.main:app --reload
Start the frontend (Streamlit)
bash
Copy
Edit
cd frontend
streamlit run Home.py
🔗 FastAPI Endpoints
Method	Route	Description
GET	/users	List all users
POST	/users	Register a new user
GET	/scores/live	Get current NBA scores
📦 Requirements
requirements.txt
txt
Copy
Edit
fastapi
uvicorn
requests
python-dotenv
streamlit
streamlit-autorefresh
🔒 .env.example
env
Copy
Edit
# Rename this file to .env and insert your MySportsFeeds key
MYSPORTS_API_KEY=Basic your_base64_api_key_here

📌 Notes
Activate the NBA feed in your MySportsFeeds account

Free tier supports only current season live scores

CORS config may be added if Streamlit is deployed independently

🛠 Future Plans
Add player stats & team logos

Historical score tracking

OAuth login & dashboards

Push notifications or email alerts

🤝 Credits
FastAPI

Streamlit

MySportsFeeds

Uvicorn

Pydantic
