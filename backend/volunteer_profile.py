from fastapi import APIRouter
import sqlite3

# This line is critical!
router = APIRouter()

@router.post("/volunteer")
def register_volunteer(name: str, skills: str, radius: int, availability: str):
    conn = sqlite3.connect("neighbourhoodcare.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO volunteers (name, skills, radius, availability) VALUES (?, ?, ?, ?)",
        (name, skills, radius, availability)
    )
    conn.commit()
    conn.close()
    return {"message": "Volunteer registered successfully"}

