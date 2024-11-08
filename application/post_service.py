from domain.post import Post
from infrastructure.post_repository import PostRepository


class PostService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def create_post(self, title: str, content: str, user_id: int) -> Post:
        post = Post(title=title, content=content, user_id=user_id)
        return self.post_repository.save(post)
    
    