from app.model import db
from app.model.user import User
from app.service.exceptions import ApiNotFound
from flask_restx import Namespace, Resource, fields

ns = Namespace("user_namespace")

user_model = ns.model("UserModel", {"user_nm": fields.String, "id": fields.Integer})


@ns.route("/")
class UserResource(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        users = db.session.query(User).all()
        if len(users) == 0:
            raise ApiNotFound(description="User(s) nor found")
        return users, 200
