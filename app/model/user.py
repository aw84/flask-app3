from app.model import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_nm = db.Column(db.String)
