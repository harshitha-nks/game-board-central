import os, json, eventlet
eventlet.monkey_patch()

from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO, join_room, emit
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import redis
from datetime import datetime

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@postgres:5432/gamedb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class GameRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(64), nullable=False)
    winner = db.Column(db.String(1))
    moves = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

redis_client = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, decode_responses=True)

socketio = SocketIO(app, cors_allowed_origins="*", message_queue='redis://redis:6379')

@app.before_first_request
def initialize():
    db.create_all()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)

    if not redis_client.exists(room):
        game = {'board': [''] * 9, 'turn': 'X', 'players': []}
        redis_client.set(room, json.dumps(game))

    game = json.loads(redis_client.get(room))

    if len(game['players']) < 2:
        game['players'].append(request.sid)
        mark = 'X' if len(game['players']) == 1 else 'O'
        redis_client.set(room, json.dumps(game))
        emit('joined', {'mark': mark}, room=request.sid)
        emit('update', game, room=room)
    else:
        emit('full', room=request.sid)

@socketio.on('chat')
def handle_chat(data):
    room = data['room']
    msg = data['message']
    emit('chat', {'message': msg, 'sid': request.sid}, room=room)

@socketio.on('move')
def handle_move(data):
    room = data['room']
    idx = data['index']
    sid = request.sid

    game = json.loads(redis_client.get(room)) if redis_client.exists(room) else None
    if not game or sid not in game['players']:
        return

    mark = 'X' if sid == game['players'][0] else 'O'
    if game['turn'] != mark or game['board'][idx] != '':
        return

    game['board'][idx] = mark
    game['turn'] = 'O' if mark == 'X' else 'X'

    winner = check_winner(game['board'])

    if winner:
        emit('game_over', {'winner': winner}, room=room)
        redis_client.delete(room)
        db.session.add(GameRecord(room=room, winner=winner, moves=len([c for c in game['board'] if c])))
        db.session.commit()
    elif '' not in game['board']:
        emit('game_over', {'winner': 'Tie'}, room=room)
        redis_client.delete(room)
        db.session.add(GameRecord(room=room, winner='T', moves=9))
        db.session.commit()
    else:
        redis_client.set(room, json.dumps(game))
        emit('update', game, room=room)

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] != '':
            return board[i]
    return None

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
