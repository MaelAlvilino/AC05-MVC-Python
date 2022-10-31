from flask import Flask
from flask_cors import CORS
import datetime
from config.enviroment import JWT_SECRET_KEY 

def creat_app():
    app = Flask(__name__)
    app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['Access-Control-Allow-Origin'] = '*'
    app.config['Access-Control-Allow-Credentials'] = True
    app.config['CORS_HEADERS'] = ['Content-Type']
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['PROPAGATE_EXCEPTIONS'] = True
    CORS(app, supports_credentials=True)

    return app