from time import sleep
from flask import Flask
from app.infrastructure.database import db
from app.api.routes import api_bp
from app.config import Config
from app.domain.user import User
from app.domain.post import Post

app = Flask(__name__)
app.config.from_object(Config)

sleep(3)

db.init_app(app)
app.register_blueprint(api_bp)

@app.before_first_request
def init_db():
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)