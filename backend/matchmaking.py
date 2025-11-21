from fastapi import APIRouter
import sqlite3
from geopy.distance import geodesic

router = APIRouter()

def score_volunteer(volunteer, task, requester_location):
    # Simplified scoring logic
    score = 0
    if task.lower() in volunteer[2].lower():  # skill match
        score += 0.4
    if volunteer[4] == "available":
        score += 0.3
    # Mock distance scoring
    score += 0.3
    return score

@router.get("/match/{request_id}")
def match_volunteer(request_id: int):
    conn = sqlite3.connect("neighbourhoodcare.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM requests WHERE id=?", (request_id,))
    request = cursor.fetchone()

    cursor.execute("SELECT * FROM volunteers")
    volunteers = cursor.fetchall()

    scored = [(v, score_volunteer(v, request[4], request[3])) for v in volunteers]
    best = max(scored, key=lambda x: x[1])

    explanation = f"Selected {best[0][1]}: skill match={request[4]}, availability={best[0][4]}, score={best[1]}"
    conn.close()

    return {"volunteer": best[0][1], "explanation": explanation}

