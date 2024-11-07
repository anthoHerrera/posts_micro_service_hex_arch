from sqlalchemy import Column, Integer, String, ForeignKey
from app.infrastructure.database import Base
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    author = relationship("User", back_ref="posts", lazy=True)

    def __repr__(self):
        return f"<Post {self.title})>"
