import React from 'react';
import './Board.css';

function Board({ board, onClick }) {
  return (
    <div className="board">
      {board.map((cell, idx) => (
        <div key={idx} className="cell" onClick={() => onClick(idx)}>
          {cell}
        </div>
      ))}
    </div>
  );
}

export default Board;
