import React, { useState, useEffect } from 'react';
import './Chat.css';

function Chat({ socket, room }) {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    socket.on('chat', (data) => {
      setMessages((prev) => [...prev, data]);
    });

    return () => {
      socket.off('chat');
    };
  }, [socket]);

  const sendMessage = () => {
    if (message.trim()) {
      socket.emit('chat', { room, message });
      setMessage('');
    }
  };

  return (
    <div className="chat-box">
      <div className="messages">
        {messages.map((m, idx) => (
          <div key={idx}><b>{m.sid.slice(0, 5)}</b>: {m.message}</div>
        ))}
      </div>
      <div className="input-area">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type a message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default Chat;