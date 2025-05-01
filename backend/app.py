import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_cors import CORS
from dotenv import load_dotenv
from config import Config
from models.user import db, User
from chat_history import ChatHistory  # Make sure this model exists
from routes.auth_routes import auth_bp
from routes.chatbot_routes import chatbot_bp

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS for frontend requests
CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")

# Initialize database
db.init_app(app)

# Initialize JWT
jwt = JWTManager(app)

# Create database tables
with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")

# --- Chat History Endpoint ---
@app.route('/api/chatbot/history', methods=['GET'])
@jwt_required()
def chat_history():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(email=user_identity['email']).first()
    history = ChatHistory.query.filter_by(user_id=user.id).order_by(ChatHistory.timestamp.desc()).all()
    return jsonify([
        {
            'question': chat.question,
            'answer': chat.answer,
            'timestamp': chat.timestamp.isoformat()
        }
        for chat in history
    ])

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)