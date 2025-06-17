import React, { useState } from 'react';
import Game from './Game';

function App() {
  const [room, setRoom] = useState('');
  const [joined, setJoined] = useState(false);

  return (
    <div>
      {!joined ? (
        <div style={{ padding: 20 }}>
          <h2>Enter Room ID</h2>
          <input value={room} onChange={e => setRoom(e.target.value)} />
          <button onClick={() => setJoined(true)}>Join Game</button>
        </div>
      ) : (
        <Game room={room} />
      )}
    </div>
  );
}

export default App;
