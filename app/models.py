from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    path = db.Column(db.String(200), nullable=False)

