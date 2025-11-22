# NeighbourhoodCare 🏡

NeighbourhoodCare is a **multi‑agent volunteer matching system** designed to support elderly and vulnerable people in local communities.  
It connects help requests with available volunteers using fairness, explainability, and transparency.

---

## 🚀 Features
- **Request Intake Agent** – collects requests from community members.
- **Volunteer Profile Agent** – registers volunteers with skills, radius, and availability.
- **Matchmaking Agent** – selects the best volunteer using explainable scoring.
- **Scheduler Agent** – assigns volunteers to requests.
- **Follow‑up Agent** – records feedback and ratings.

---

## 📦 Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/vishnu-prasad-g-s/NeighbourhoodCare.git
cd NeighbourhoodCare/backend

python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

cd backend
python3 -m uvicorn main:app --reload

