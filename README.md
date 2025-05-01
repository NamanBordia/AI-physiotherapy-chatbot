# AI Physiotherapy Chatbot 🤖🏥

A full-stack AI-powered chatbot designed to assist users with physiotherapy-related queries.  
Built with Flask, React, JWT authentication, and integrates advanced NLP models.

---

## 🚀 Features

- **User Authentication:** Secure signup/login with JWT tokens.
- **Personalized Chat:** Each user gets their own chat history.
- **AI-Powered Answers:** Uses advanced models (e.g., BioBERT, Cohere) for physiotherapy Q&A.
- **Chat History Sidebar:** View, rename, and revisit previous chats.
- **Responsive UI:** Built with React for a smooth user experience.
- **API Key & Model Security:** Secrets and large files are kept out of the repo.

---

## 🛠️ Tech Stack

- **Frontend:** React, JavaScript, CSS
- **Backend:** Flask, Flask-JWT-Extended, SQLAlchemy, Flask-Bcrypt
- **Database:** MySQL (or your preferred RDBMS)
- **AI/NLP:** Cohere API, BioBERT (local or cloud)
- **Authentication:** JWT (JSON Web Tokens)

---

## ⚡ Quick Start

### 1. Clone the Repository

```sh
git clone https://github.com/NamanBordia/AI-physiotherapy-chatbot.git
cd AI-physiotherapy-chatbot
```

### 2. Backend Setup

- Create a virtual environment and activate it:
  ```sh
  python -m venv venv
  venv\Scripts\activate  # On Windows
  # or
  source venv/bin/activate  # On Mac/Linux
  ```
- Install dependencies:
  ```sh
  pip install -r backend/requirements.txt
  ```
- Set up your `.env` file in `backend/` (see [Environment Variables](#-environment-variables)).
- Run database migrations (if needed).
- Start the backend:
  ```sh
  cd backend
  python app.py
  ```

### 3. Frontend Setup

```sh
cd frontend
npm install
npm start
```
The frontend will run on [http://localhost:3000](http://localhost:3000).

---

## 🔑 Environment Variables

Create a `.env` file in your `backend/` directory with the following:

```env
SECRET_KEY=your_flask_secret
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URI=mysql+pymysql://user:password@localhost/ai_physio_db
COHERE_API_KEY=your_cohere_api_key
BIOBERT_MODEL_PATH=path/to/biobert/model
```

**Never commit your `.env` or API keys to git!**

---

## 📁 Project Structure

```
AI-physiotherapy-chatbot/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models/
│   ├── routes/
│   ├── chat_history.py
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── ...
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📝 Usage

1. **Sign up or log in** to get your JWT token.
2. **Start chatting** with the AI physiotherapy assistant.
3. **View and rename** your chat history in the sidebar.

---

## 🧑‍💻 Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 🛡️ Security & Best Practices

- All secrets and large files are excluded via `.gitignore`.
- Use environment variables for all API keys and sensitive data.
- Never commit model weights or API keys to the repository.

---

## 📄 License

[MIT](LICENSE)

---

## 🙏 Acknowledgements

- [Cohere](https://cohere.com/)
- [BioBERT](https://github.com/dmis-lab/biobert)
- [Flask](https://flask.palletsprojects.com/)
- [React](https://reactjs.org/)

---

> **Maintained by [Naman Bordia](https://github.com/NamanBordia)**
