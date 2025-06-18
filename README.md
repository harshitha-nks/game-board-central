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
- Real-time chat between players
- Automatic state synchronization between players
- Reconnection-safe architecture
- Persistent game history in PostgreSQL
- In-memory state caching via Redis

---

## Tech Stack

| Layer      | Technology         | Description                                |
|------------|--------------------|--------------------------------------------|
| Frontend   | React              | Component-based UI for game and lobby      |
| Backend    | Flask + Flask-SocketIO | WebSocket server to manage game state     |
| Transport  | Socket.IO          | Real-time duplex communication              |
| Database   | PostgreSQL         | Persistent storage of game records     |
| Cache/Queue| Redis              | In-memory state and real-time message broadcasting |
| Styling    | CSS Grid           | Clean and responsive game layout           |
|  DevOps    | Docker + Docker Compose| Containerized full-stack deployment    |

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
## Running the Application with Docker
Ensure Docker and Docker Compose are installed
```
docker-compose up --build
```
This will spin up:
- Frontend on http://localhost:3000
- Backend on http://localhost:5000
- PostgreSQL on port 5432
- Redis on port 6379

### To stop docker and clean up
```
docker-compose down
```
This stops all containers and removes associated networks.
Use --volumes if you also want to delete volumes:
```
docker-compose down --volumes
```
---
## How to Play
1. Open http://localhost:3000 in two separate browser windows or devices.
2. Enter the same Room ID in both windows or devices. 
3. Play Tic Tac Toe in real-time with full synchronization and chat.
---
## Features
- Real-time gameplay with Socket.IO
- Game logic handled server-side
- Room-based matchmaking
- Fast and responsive UI
- Win/Tie detection
- Handles page refreshes mid-game









