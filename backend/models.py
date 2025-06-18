from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GameRecord(db.Model):
    __tablename__ = 'game_records'
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(64), index=True)
    winner = db.Column(db.String(1))
    moves = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
