# 🏀 Creature Report - Live Sports Dashboard

Creature Report is a Bleacher Report-style web app that displays live NBA scores, lets users register with their favorite team, and filters content accordingly. Built with **FastAPI**, **Streamlit**, **PostgreSQL**, and powered by real-time data from the **ESPN API**.

---

## ⚙️ Features

✅ FastAPI backend with PostgreSQL  
✅ Streamlit multipage dashboard (Live Scores, Users)  
✅ Auto-refreshing NBA scoreboard with filters  
✅ Toggle for dark mode  
✅ Docker + `.env` + volume persistence  
✅ User registration & team tracking

---

## 📁 Project Structure

```bash
CreatureReport/
├── .env                   # API keys, DB config
├── .env.example           # Template file
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yaml
├── src/
│   └── backend/
│       ├── main.py
│       ├── database.py
│       ├── models/
│       │   └── user_model.py
│       ├── routers/
│       │   ├── user_routers.py
│       │   └── score_routers.py
│       └── services/
│           └── espn.py
└── frontend/
    ├── Home.py
    ├── pages/
    │   ├── LiveScores.py
    │   └── Users.py
    └── .streamlit/
        └── config.toml
```

---

## 🚀 Getting Started (Locally)

### 1. Clone the Repo

```bash
git clone https://github.com/Jthomas0521/CreatureReport.git
cd CreatureReport
```

### 2. Set up Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` with your ESPN or app-specific secrets.

---

## 🐳 Docker Setup

### Build & Run Everything

```bash
docker-compose up --build
```

- Backend: [http://localhost:8000](http://localhost:8000)  
- Frontend: [http://localhost:8501](http://localhost:8501)

---

## 🔗 FastAPI Endpoints

| Method | Route         | Description              |
|--------|---------------|--------------------------|
| GET    | `/users`      | Get all registered users |
| POST   | `/users`      | Register new user        |
| GET    | `/scores/live`| Get current NBA scores   |

---

## 📦 Requirements

```
fastapi
uvicorn
sqlalchemy
psycopg2-binary
streamlit
streamlit-autorefresh
requests
python-dotenv
```

---

## 🔒 .env Example

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/bleacher_db
ESPN_API_URL=http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard
```

---

## 🧠 Notes

- ESPN's public API doesn't require auth for scoreboard endpoint
- Make sure port `5432` is not in use locally if running Docker
- Streamlit auto-refreshes every 60s on LiveScores page
- Team filters update dynamically from ESPN data

---

## 🛠 Future Plans

- Add player box scores and stat tracking  
- Support user dashboards + auth  
- Track user preferences in PostgreSQL  
- Email/Push notifications for favorite teams  
- Season/game filtering options

---

## 🤝 Credits

- [FastAPI](https://fastapi.tiangolo.com/)  
- [Streamlit](https://streamlit.io)  
- [Uvicorn](https://www.uvicorn.org/)  
- [PostgreSQL](https://www.postgresql.org/)  
- [ESPN Scoreboard API](http://site.api.espn.com)  