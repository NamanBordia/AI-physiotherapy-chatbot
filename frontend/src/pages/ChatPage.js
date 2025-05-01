import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Chatbot from "../components/Chatbot";

function ChatPage() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [chatHistory, setChatHistory] = useState([]);
  const [selectedChat, setSelectedChat] = useState(null);
  const [renamingId, setRenamingId] = useState(null);
  const [renameValue, setRenameValue] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
    } else {
      setUser(token);
      fetch("/api/chatbot/history", {
        headers: { Authorization: `Bearer ${token}` },
      })
        .then((res) => res.json())
        .then((data) => setChatHistory(data))
        .catch(() => setChatHistory([]));
    }
    setLoading(false);
  }, [navigate]);

  const handleRename = async (chatId) => {
    const token = localStorage.getItem("token");
    await fetch(`/api/chatbot/chat/${chatId}/rename`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ chat_name: renameValue }),
    });
    setChatHistory((prev) =>
      prev.map((chat) =>
        chat.id === chatId ? { ...chat, chat_name: renameValue } : chat
      )
    );
    setRenamingId(null);
    setRenameValue("");
  };

  if (loading) return <p>Loading...</p>;

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      {/* Sidebar for Chat History */}
      <div style={{ width: "300px", background: "#f5f5f5", borderRight: "1px solid #ddd", padding: "1rem", overflowY: "auto" }}>
        <h3>Chat History</h3>
        <ul style={{ listStyle: "none", padding: 0 }}>
          {chatHistory.length === 0 && <li>No chat history found.</li>}
          {chatHistory.map((chat) => (
            <li
              key={chat.id}
              style={{
                marginBottom: "1rem",
                cursor: "pointer",
                background: selectedChat === chat.id ? "#e0e0e0" : "transparent",
                padding: "0.5rem",
                borderRadius: "5px",
                position: "relative"
              }}
              onClick={() => setSelectedChat(chat.id)}
            >
              {renamingId === chat.id ? (
                <span>
                  <input
                    value={renameValue}
                    onChange={(e) => setRenameValue(e.target.value)}
                    onClick={(e) => e.stopPropagation()}
                  />
                  <button onClick={(e) => { e.stopPropagation(); handleRename(chat.id); }}>Save</button>
                  <button onClick={(e) => { e.stopPropagation(); setRenamingId(null); }}>Cancel</button>
                </span>
              ) : (
                <span>
                  <strong>{chat.chat_name}</strong>
                  <button
                    style={{ marginLeft: 8 }}
                    onClick={(e) => { e.stopPropagation(); setRenamingId(chat.id); setRenameValue(chat.chat_name); }}
                  >✏</button>
                </span>
              )}
              <br />
              <small>{new Date(chat.timestamp).toLocaleString()}</small>
            </li>
          ))}
        </ul>
      </div>

      {/* Main Chat Area */}
      <div style={{ flex: 1, padding: "2rem" }}>
        <h2>AI Physiotherapy Chatbot</h2>
        {user ? (
          selectedChat !== null ? (
            <div>
              <h4>Question:</h4>
              <p>{chatHistory.find((c) => c.id === selectedChat)?.question}</p>
              <h4>Answer:</h4>
              <p>{chatHistory.find((c) => c.id === selectedChat)?.answer}</p>
              <button onClick={() => setSelectedChat(null)}>Back to Chat</button>
            </div>
          ) : (
            <Chatbot />
          )
        ) : (
          <p>You must be logged in to access the chatbot.</p>
        )}
      </div>
    </div>
  );
}

export default ChatPage;
