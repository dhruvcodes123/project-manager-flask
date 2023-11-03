from http import HTTPStatus

from flask import make_response
from marshmallow import ValidationError

from .models import Projects
from .schemas import ProjectSchema

project_schema = ProjectSchema()
project_response_schema = ProjectSchema(load_only=('created_at',))


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
            task = schema.load(data)
            if not task['title']:
                return False, {"message": "Title should not be empty."}
            return True, task
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


_serializer = Serializer()
