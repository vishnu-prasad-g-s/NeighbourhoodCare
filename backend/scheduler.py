from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.post("/schedule")
def schedule_task(request_id: int, volunteer_id: int):
    conn = sqlite3.connect("neighbourhoodcare.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE requests SET status='assigned' WHERE id=?", (request_id,))
    conn.commit()
    conn.close()

    return {"message": f"Volunteer {volunteer_id} assigned to request {request_id}"}

