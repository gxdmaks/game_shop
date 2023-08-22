from database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger(), autoincrement=True, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=True)
    email = db.Column(db.String(), nullable=False)
    user_city = db.Column(db.String(), nullable=True)


class Games(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True )
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    prices = db.Column(db.Float(), nullable=False)
    link = db.Column(db.String(), nullable=False)


