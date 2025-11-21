from fastapi import FastAPI
from intake import router as intake_router
from volunteer_profile import router as volunteer_router
from matchmaking import router as matchmaking_router
from scheduler import router as scheduler_router
from followup import router as followup_router
import database

app = FastAPI(title="NeighbourhoodCare")

database.init_db()

app.include_router(intake_router)
app.include_router(volunteer_router)
app.include_router(matchmaking_router)
app.include_router(scheduler_router)
app.include_router(followup_router)

