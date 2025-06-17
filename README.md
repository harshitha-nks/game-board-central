# Game Board Central 

**Game Board Central** is a distributed, real-time multiplayer **Tic Tac Toe** web application that allows two users to play interactively over a shared room. The application is built using a **React frontend** and a **Flask-SocketIO backend**, enabling low-latency communication between geographically dispersed players via WebSockets.

This project demonstrates full-stack development, real-time distributed system communication, and room-based game state synchronization.

---

## Game Description

Tic Tac Toe is a classic 3x3 grid game played between two players who alternate turns placing their respective symbols (**X** and **O**) on the board. The first player to align three of their symbols in a row — horizontally, vertically, or diagonally — wins the game. If the board is filled and no player has won, the game results in a tie.

Game Board Central supports:
- Real-time turn-by-turn gameplay
- Win and tie detection
- Room-based matchmaking
- Automatic state synchronization between players
- Reconnection-safe architecture

---

## Tech Stack

| Layer      | Technology         | Description                                |
|------------|--------------------|--------------------------------------------|
| Frontend   | React              | Component-based UI for game and lobby      |
| Backend    | Flask + Flask-SocketIO | WebSocket server to manage game state     |
| Transport  | Socket.IO          | Real-time duplex communication              |
| Styling    | CSS Grid           | Clean and responsive game layout           |

---

## Running the Application Locally

### Backend (Flask)

```
cd backend
pip install -r requirements.txt
python app.py
```
- Runs on http://localhost:5000
### Frontend (React)
```
cd frontend
npm install
npm start
```
- Runs on http://localhost:3000
---
## How to Play
1. Open http://localhost:3000 in two separate browser windows or devices.
2. Enter the same Room ID in both windows.
3. Start playing real-time Tic Tac Toe.
---
## Features
- Real-time gameplay with Socket.IO
- Game logic handled server-side
- Room-based matchmaking
- Fast and responsive UI
- Win/Tie detection
- Handles page refreshes mid-game









