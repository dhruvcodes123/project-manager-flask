from http import HTTPStatus

from flask import make_response
from marshmallow import ValidationError

from .models import Projects
from .schemas import ProjectSchema, _project_schema, ProjectUpdateSchema
from ...constants import CONTENT_NOT_FOUND_MESSAGE

project_schema = ProjectSchema()
project_response_schema = ProjectSchema(load_only=('created_at',))
project_update_request_schema = ProjectUpdateSchema(partial=True)


class Serializer:
    @staticmethod
    def load(data, schema):
        """
        Loads the JSON data to model object.

        schema: marshmallow schema object.
            Responsible for serializing of JSON data in model object.
            Validates the schema and returns Errors.
        Return:
            boolean: True or False
            Python Dictionary of data or Error Messages
        """
        try:
            if data is None:
                data = {}
            project = schema.load(data)
            if not project['title']:
                return False, {"message": "Title should not be empty."}
            return True, project
        except ValidationError as e:
            return False, e.messages

    @staticmethod
    def dump(data, schema, extra_args=None):
        """
        Converts model object to JSON serializable data.

        schema: marshmallow schema object.
            Responsible for serializing of JSON data in model object.
            Validates the schema and returns Errors.
        extra_args: Python dictionary
            Contains extra information to be added in response data.
        Return
            JSON serializable data.
        """
        data = schema.dump(data)
        if extra_args:
            data.update(extra_args)
        return data


class ProjectServices:

    def __init__(self, request):
        self.request = request

    def create(self):
        """
        Create a new project using provided data.
        """
        data = self.request.get_json(force=True, silent=True)
        is_valid, data_or_errors = _serializer.load(data, project_schema)

        if is_valid:
            response = Projects.save(data_or_errors)
            json_response = _serializer.dump(response, project_response_schema)
            return make_response({'data': json_response,
                                  'message': 'Project created successfully.'}, HTTPStatus.CREATED)

        return make_response(data_or_errors, HTTPStatus.BAD_REQUEST)

    def get(self):
        """
        Calls the model get method and Serializes in required formate response.
        Return:
            JSON Response, HTTP status code
        """
        values = self.request.args.to_dict()
        try:
            data = Projects.get()
        except KeyError as e:
            return make_response({"error": f'Invalid field {e}'}, HTTPStatus.BAD_REQUEST)
        except ValidationError as e:
            return make_response({'message': e.messages}, HTTPStatus.BAD_REQUEST)
        return make_response(
            {'data': _project_schema.dump(data, many=True), 'message': 'Projects fetched successfully.'},
            HTTPStatus.OK)

    def get_by_id(self, id):
        """
        Calls the model get_by_id method and Serializes in required formate response.
        Parameter
        ---------
        id: id of the project
        Return
        ------
        JSON Response, HTTP status code
        """
        data = Projects.get_by_id(id)
        if not data:
            return make_response({'message': CONTENT_NOT_FOUND_MESSAGE}, HTTPStatus.NOT_FOUND)
        json_response = _serializer.dump(data, project_response_schema)
        return make_response({'data': json_response, 'message': 'Project fetched successfully.'}, HTTPStatus.OK)

    def update(self, id):
        """
        Calls the model update method and Serializes in required formate response.
        Parameter:
            id: id of the Project
        Return:
            JSON Response, HTTP status code
        """
        project = Projects.get_by_id(id)
        data = self.request.get_json(silent=True)
        if project:
            is_valid, data_or_errors = Serializer.load(data, project_update_request_schema)
            if is_valid:
                response = project.update(data_or_errors)
                json_response = _project_schema.dump(response)
                return make_response({'data': json_response, 'message': 'Project updated successfully.'}, HTTPStatus.OK)

            return make_response({'message': data_or_errors}, HTTPStatus.BAD_REQUEST)

        return make_response({'message': CONTENT_NOT_FOUND_MESSAGE}, HTTPStatus.NOT_FOUND)


_serializer = Serializer()
