from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

games = {}  # room_id -> {'board': [...], 'turn': 'X', 'players': []}

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)

    if room not in games:
        games[room] = {'board': [''] * 9, 'turn': 'X', 'players': []}

    if len(games[room]['players']) < 2:
        games[room]['players'].append(request.sid)
        emit('joined', {'mark': 'X' if len(games[room]['players']) == 1 else 'O'}, room=request.sid)
        emit('update', games[room], room=room)
    else:
        emit('full', room=request.sid)

@socketio.on('move')
def handle_move(data):
    room = data['room']
    idx = data['index']
    sid = request.sid
    game = games.get(room)

    if not game or sid not in game['players']:
        return

    current_mark = 'X' if sid == game['players'][0] else 'O'

    if game['turn'] != current_mark or game['board'][idx] != '':
        return

    game['board'][idx] = current_mark
    game['turn'] = 'O' if current_mark == 'X' else 'X'

    winner = check_winner(game['board'])
    if winner:
        emit('game_over', {'winner': winner}, room=room)
        games.pop(room)
    elif '' not in game['board']:
        emit('game_over', {'winner': 'Tie'}, room=room)
        games.pop(room)
    else:
        emit('update', game, room=room)

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] != '':
            return board[i]
    return None

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
