
from flask_restful import Api
from config.app_config import creat_app
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from models.users import User



app = creat_app()

api = Api(app)

jwt = JWTManager(app)
db = SQLAlchemy(app)

@app.before_first_request
def criaBanco():
    db.create_all()


@app.route('/', methods=['GET'])
def teste():
    return {"version": "1.0.0"}

# Rotas
@app.route('/users', methods=['GET','POST'])
def get_users():
    users = User.find_by_users()
    if not users: return []
    return users.json()

if __name__ == "__main__":
    app.run('0.0.0.0', port=4000)