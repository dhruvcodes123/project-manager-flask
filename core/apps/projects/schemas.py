from marshmallow import fields

from core import marshmallow
from .models import Projects


class ProjectSchema(marshmallow.SQLAlchemyAutoSchema):
    """
    Serializer for the projects model.
    """

    class Meta:
        model = Projects


class SubProjectResponseSchema(marshmallow.SQLAlchemyAutoSchema):
    """
    Serializer for the Project model.
    Used for serializing the children attribute of parent tasks.
    """

    class Meta:
        include_fk = True
        model = Projects


class ProjectFilterSchema(marshmallow.SQLAlchemyAutoSchema):
    """
    Serializes the filtering the Projects.
    """

    class Meta:
        model = Projects
        include_fk = True
        fields = ['id', 'title', 'description', "completed", "created_at"]

    children = fields.Nested(SubProjectResponseSchema, many=True)


_task_schema = ProjectFilterSchema()
