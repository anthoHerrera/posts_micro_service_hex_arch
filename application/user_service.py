from typing import List
from domain.user import User
from infrastructure.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        return self.user_repository.save(user)
    
    def get_user_by_id(self, user_id: int) -> List[User]:
        return self.user_repository.get_by_id(user_id)
    
    def get_user_by_email(self, email: str) -> List[User]:
        return self.user_repository.get_by_email(email)