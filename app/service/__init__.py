from app.service.task import ns as task_ns
from app.service.user import ns as user_ns
from flask_restx import Api

api = Api()

api.add_namespace(user_ns)
api.add_namespace(task_ns)
