from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.context_retrieval import answer_question
from models.user import User, db
from chat_history import ChatHistory
from datetime import datetime

chatbot_bp = Blueprint("chatbot", __name__)
@chatbot_bp.route("/chat", methods=["POST"])
def chat():
    try:
        # Get the user query from the request
        data = request.get_json()
        user_query = data.get("query", "")

        if not user_query:
            return jsonify({"error": "Query is required"}), 400

        # Get the answer and context
        answer, context = answer_question(user_query)
        

        # Return the response as JSON
        return jsonify({"answer": answer, "context": context})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@chatbot_bp.route("/history", methods=["GET"])
@jwt_required()
def chat_history():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(email=user_identity['email']).first()
    history = ChatHistory.query.filter_by(user_id=user.id).order_by(ChatHistory.timestamp.desc()).all()
    return jsonify([
        {
            'id': chat.id,
            'question': chat.question,
            'answer': chat.answer,
            'timestamp': chat.timestamp.isoformat(),
            'chat_name': chat.chat_name
        }
        for chat in history
    ])

@chatbot_bp.route("/chat/<int:chat_id>/rename", methods=["POST"])
@jwt_required()
def rename_chat(chat_id):
    data = request.get_json()
    new_name = data.get("chat_name")
    chat = ChatHistory.query.get(chat_id)
    if chat:
        chat.chat_name = new_name
        db.session.commit()
        return jsonify({"success": True, "chat_name": new_name})
    return jsonify({"success": False, "error": "Chat not found"}), 404