from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.post("/request")
def create_request(name: str, phone: str, address: str, task: str, urgency: str):
    conn = sqlite3.connect("neighbourhoodcare.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO requests (name, phone, address, task, urgency) VALUES (?, ?, ?, ?, ?)",
                   (name, phone, address, task, urgency))
    conn.commit()
    conn.close()
    return {"message": "Request submitted successfully"}

