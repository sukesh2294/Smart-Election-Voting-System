# init_db.py

from app import app, db
from models import Candidate  # Optional: also import Admin, Voter if you want all tables

with app.app_context():
    print("🛠️ Recreating all tables...")
    db.create_all()

    print("✅ Database reset successful.")

