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


projects_api.add_resource(CreateProject, '/create-project')
