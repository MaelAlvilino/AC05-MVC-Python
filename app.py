

from config.app_config import creat_app
from flask_jwt_extended import JWTManager
from model.user import User
from db.database import Database
from flask import request
from model.user import User



app = creat_app()

app.config['database'] = Database(create_all=True)


jwt = JWTManager(app)


@app.route('/', methods=['GET'])
def teste():
    return {"version": "1.0.0"}

# Rotas
@app.route('/users', methods=['GET','POST'])
def user_view():
    print(request.get_json())
    if request.method == 'POST':
        print('entrei aqui')
        user = User(
            email= request.get_json()['email'],
            password= request.get_json()['password']
        )
        
        dbsession = app.config['database'].session_scoped()
        dbsession.add(user)
        dbsession.commit()
        app.config['database'].session_scoped.remove()
        return 'Tudo certo', 201

    if request.method == 'GET':
        users = User.find_by_users()
        if not users: return []
        return users.json()

if __name__ == "__main__":
    app.run('0.0.0.0', port=4000, debug=True) 