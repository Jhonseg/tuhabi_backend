from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

from app.consulta import consulta_bp
from app.like import like_bp

app.register_blueprint(consulta_bp, url_prefix='/api/v1')
app.register_blueprint(like_bp, url_prefix='/api/v1')