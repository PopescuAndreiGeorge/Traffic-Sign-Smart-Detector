from flask_sqlalchemy import SQLAlchemy  # pip install flask_sqlalchemy

db = SQLAlchemy()

class YourModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    # Define other fields and methods as needed
