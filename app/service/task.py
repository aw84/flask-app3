from app.celery.tasks import test_task
from flask_restx import Namespace, Resource

ns = Namespace("task_namespace")


@ns.route("/")
class Task(Resource):
    def get(self):

        id = test_task.apply_async(args=(1, 3))
        return f"OK {id}", 200
