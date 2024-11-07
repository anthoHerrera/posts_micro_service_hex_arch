from sqlalchemy import Column, Integer, String
from app.infrastructure.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    
    def __repr__(self):
        return f"<User {self.name})>"
    