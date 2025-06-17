import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import Board from './Board';

const socket = io('http://localhost:5000');

function Game({ room }) {
  const [game, setGame] = useState(null);
  const [mark, setMark] = useState(null);
  const [status, setStatus] = useState('');

  useEffect(() => {
    socket.emit('join', { room });

    socket.on('joined', data => setMark(data.mark));
    socket.on('full', () => setStatus('Room is full'));
    socket.on('update', data => setGame(data));
    socket.on('game_over', data => {
      if (data.winner === 'Tie') {
        setStatus("It's a tie!");
      } else {
        setStatus(`${data.winner} wins!`);
      }
    });

    return () => socket.disconnect();
  }, [room]);

  const handleMove = idx => {
    if (game.board[idx] === '' && game.turn === mark) {
      socket.emit('move', { room, index: idx });
    }
  };

  return (
    <div>
      <h3>You are: {mark}</h3>
      <h3>{status || `Turn: ${game?.turn}`}</h3>
      <Board board={game?.board || []} onClick={handleMove} />
    </div>
  );
}

export default Game;
