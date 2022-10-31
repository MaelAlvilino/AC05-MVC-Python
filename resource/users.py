
from flask_restful import Resource,reqparse
from models.users import User

class UserResource(Resource):
    def post(self):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('username', type=str, required=True,
                                help="O campo 'username' não pode estar em branco.") 
        argumentos.add_argument('email', type=str, required=True,
                                help="O campo 'email' não pode estar em branco.") 
        dados = argumentos.parse_args()

        user = User(**dados)
        user.save()
        return {""}
    def get(self):
        users = User.find_by_users()
        if not users: return []
        return users.json()