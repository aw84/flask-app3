from flask_restx import fields, Resource, Namespace
from app.model import db

ns = Namespace("user_namespace")
from app.model.user import User

user_list = ns.model("UserListModel", {"user_nm": fields.String, "id": fields.Integer})


@ns.route("/")
class UserResource(Resource):
    @ns.marshal_list_with(user_list)
    def get(self):
        users = db.session.query(User).all()
        return users, 200
