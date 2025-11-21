from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.post("/feedback")
def collect_feedback(request_id: int, rating: int, comments: str):
    conn = sqlite3.connect("neighbourhoodcare.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE requests SET status='completed' WHERE id=?", (request_id,))
    conn.commit()
    conn.close()

    return {"message": f"Feedback recorded for request {request_id}", "rating": rating, "comments": comments}

