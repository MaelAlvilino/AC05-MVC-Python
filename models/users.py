from db.config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username=None, email = None):
        self.username = username
        self.email = email
    
    def json(self):
        return{
            "username": self.username,
            "email": self.email
        }
    
    @classmethod
    def find_by_users(cls):
        users = cls.query.filter_by().all()
        if users:
            return users
        return None
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
