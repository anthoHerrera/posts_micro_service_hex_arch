from time import sleep
from flask import Flask
from infrastructure.database import db
from api.routes import api_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

sleep(3)

db.init_app(app)
app.register_blueprint(api_bp)

with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    