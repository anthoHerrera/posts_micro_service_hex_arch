from flask import Blueprint, request, jsonify
from application.user_service import UserService
from application.post_service import PostService
from infrastructure.user_repository import UserRepository
from infrastructure.post_repository import PostRepository
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
    return jsonify(user.to_dict()), 201
@api_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404
    return jsonify(user.to_dict()), 200

@api_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404
    user_service.delete_user(user_id)
    return jsonify({"message": "user deleted"}), 200

@api_bp.route("/posts", methods=["POST"])
def create_post():
    data  = request.json
    if not data.get("title") or not data.get("content") or not data.get("user_id"):
        return jsonify({"error": "title, content and user_id are required"}), 400
    post = post_service.create_post(data["title"], data["content"], data["user_id"])
    return jsonify(post.to_dict()), 201
@api_bp.route("/posts", methods=["GET"])
def get_posts():
    posts = post_service.get_posts()
    return jsonify([post.to_dict() for post in posts]), 200
@api_bp.route("/posts/<int:user_id>", methods=["GET"])
def get_posts_by_user_id(user_id):
    posts = post_service.get_posts_by_user_id(user_id)
    return jsonify([post.to_dict() for post in posts]), 200