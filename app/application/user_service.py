from app.domain.user import User
from app.infrastructure.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        return self.user_repository.save(user)
    