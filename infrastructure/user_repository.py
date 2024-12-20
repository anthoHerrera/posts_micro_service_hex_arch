from domain.user import User
from infrastructure.database import db
class UserRepository:
    def save(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user
    
    def get_by_id(self, user_id: int) -> User:
        return User.query.get(user_id)
    
    def get_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()
    
    def delete(self, user_id: int) -> None:
        user = self.get_by_id(user_id=user_id)
        if user:
            db.session.delete(user)
            db.session.commit()