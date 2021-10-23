from app.model import db
from app.model.user import User
from app.service.exceptions import ApiNotFound
from flask_restx import Namespace, Resource, fields

ns = Namespace("user_namespace")

user_list = ns.model("UserListModel", {"user_nm": fields.String, "id": fields.Integer})


@ns.route("/")
class UserResource(Resource):
    @ns.marshal_list_with(user_list)
    def get(self):
        users = db.session.query(User).all()
        if len(users) == 0:
            raise ApiNotFound(description="User GET bad request")
        return users, 200
