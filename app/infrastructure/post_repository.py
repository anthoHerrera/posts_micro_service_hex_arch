from typing import List
from app.domain.post import Post
from app.infrastructure.database import db

class PostRepository:
    def save(self, post: Post) -> Post:
        db.session.add(post)
        db.session.commit()
        return post
    
    def get_by_user_id(self, user_id: int) -> List[Post]:
        return Post.query.filter_by(user_id=user_id).all()
    