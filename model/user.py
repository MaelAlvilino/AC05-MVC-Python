from db.base import base


from sqlalchemy import Column, String, BigInteger


class User (base):
    __tablename__ =  'USER'
    user_id = Column(BigInteger, primary_key=True)
    user_email = Column(String(60))
    user_password = Column(String(255))