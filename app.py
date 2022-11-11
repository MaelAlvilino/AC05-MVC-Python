

from config.app_config import creat_app
from flask_jwt_extended import JWTManager
from db.database import Database
from flask import request
from model.user import User
from views.user_view import User_view



app = creat_app()

app.config['database'] = Database(create_all=True)


jwt = JWTManager(app)


@app.route('/', methods=['GET'])
def teste():
    return {"version": "1.0.0"}

# Rotas
app.add_url_rule('/users', view_func=User_view.as_view('userView'))

if __name__ == "__main__":
    app.run('0.0.0.0', port=4000, debug=True) 