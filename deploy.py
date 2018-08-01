from src.main import app
from db import db

db.init_app(app)

# Create tables before the first requests gets dispatched
@app.before_first_request
def create_tables():
    db.create_all() 
    