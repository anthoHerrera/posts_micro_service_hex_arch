from flask import Blueprint, request, jsonify
from app.application.user_service import UserService
from app.application.post_service import PostService
from app.infrastructure.user_repository import UserRepository
from app.infrastructure.post_repository import PostRepository

user_repository = UserRepository()
post_repository = PostRepository()

user_service = UserService(user_repository)
post_service = PostService(post_repository)

api_bp = Blueprint("api", __name__)


@api_bp.route("/users", methods=["POST"])
def create_user():
    data  = request.json
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "name and email are required"}), 400
    user = user_service.create_user(data["name"], data["email"])
    return jsonify(user.__dict__), 201

@api_bp.route("/posts", methods=["POST"])
def create_post():
    data  = request.json
    if not data.get("title") or not data.get("content") or not data.get("user_id"):
        return jsonify({"error": "title, content and user_id are required"}), 400
    post = post_service.create_post(data["title"], data["content"], data["user_id"])
    return jsonify(post.__dict__), 201
