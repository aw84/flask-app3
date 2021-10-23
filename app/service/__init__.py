from app.service.exceptions import ApiException
from app.service.task import ns as task_ns
from app.service.user import ns as user_ns
from flask_restx import Api

api = Api()
api.add_namespace(user_ns)
api.add_namespace(task_ns)


@api.errorhandler(ApiException)
def handle_bad_request_2(e):
    response = {
        "code": e.code,
        "message": e.description,
    }

    return response, e.code
