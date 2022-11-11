from flask.views import View
from flask import request, current_app
from model.user import User
from sqlalchemy.orm import Session



class User_view(View):
    methods = ['PATCH', 'DELETE', 'GET', 'POST']
    def post(self):
        user = User(
            user_email= request.get_json().get('user_email'),
            user_password= request.get_json()['user_password'],
        )
        dbsession:Session = current_app.config['database'].session_scoped()
        dbsession.add(user)
        dbsession.commit()
        current_app.config['database'].session_scoped.remove()
        return 'Tudo certo', 200

    def get(self):
        dbsession = current_app.config['database'].session_scoped()
        if 'user_email' not in request.args:
            users = dbsession.query(User).all()
            retorno = [
                {
                    'user_email': i.user_email,
                    'user_id': i.user_id,
                }
                for i in users
            ]
            return retorno, 200

        user = dbsession.query(User).filter(User.user_email == request.args.get('user_email')).first()
        if user is None:
            return 'Bad resquet de usuario não existe', 404 
        retorno = {'user_email': user.user_email}
        current_app.config['database'].session_scoped.remove()

        return retorno, 200
    def patch(self):
        if 'user_email' not in request.args:
            return 'Bad request bobão', 400
        dbsession = current_app.config['database'].session_scoped()
        user = dbsession.query(User).filter(User.user_email == request.args.get('user_email')).first()
        if user is None:
            return 'Bad resquet de usuario não existe', 404
        user.user_email = request.get_json()['user_email']
        user.user_password = request.get_json()['user_password']
        dbsession.commit()
        current_app.config['database'].session_scoped.remove()

        return 'sucesso', 200
    def delete(self):
        if 'user_email' not in request.args:
            return 'Bad request bobão', 400
        dbsession = current_app.config['database'].session_scoped()
        user = dbsession.query(User).filter(User.user_email == request.args.get('user_email')).first()
        if user is None:
            return 'Bad resquet de usuario não existe', 404
        
        dbsession.delete(user)
        dbsession.commit()
        current_app.config['database'].session_scoped.remove()
        return 'deletamos', 200

    def dispatch_request(self):
        return getattr(self, str(request.method).lower())()
