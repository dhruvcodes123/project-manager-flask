from flask import Blueprint, request
from flask_restful import Api, Resource

from .services import ProjectServices

projects_blueprint = Blueprint('projects', __name__)
projects_api = Api(projects_blueprint)


class CreateProject(Resource):
    """
    Route handles the creation of new  Project.

    Methods:
        post(): Handles HTTP POST requests for project creation.
    """

    register_service = ProjectServices(request)

    @classmethod
    def post(cls):
        """
        Handle the HTTP POST request for project creation.
        Parameter:

        Return:
            JSON serializable data
        """
        return cls.register_service.create()

    @classmethod
    def get(cls, id=None):
        """
        Handle the HTTP GET request to view projects.
        Parameter:
            id: id of task
        Return:
            JSON serializable data
        """
        return cls.register_service.get() if id is None else cls.register_service.get_by_id(id)


projects_api.add_resource(CreateProject, '/project', '/project/<int:id>')
