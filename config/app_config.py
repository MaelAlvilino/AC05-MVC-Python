from flask import Flask
from flask_cors import CORS
import datetime
from config.enviroment import JWT_SECRET_KEY 

def creat_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
    app.config['JWT_BLACKLIST_ENABLED'] = True
    CORS(app, supports_credentials=True)

    return app