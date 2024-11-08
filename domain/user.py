from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from infrastructure.database import Base
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    posts = relationship("Post", back_populates="user", cascade="all, delete")
    
    def __repr__(self):
        return f"<User {self.name})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
        