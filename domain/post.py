from sqlalchemy import Column, Integer, String, ForeignKey
from infrastructure.database import Base
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    author = relationship("User", backref="posts", lazy=True)

    def __repr__(self):
        return f"<Post {self.title})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "user_id": self.user_id
        }
        
