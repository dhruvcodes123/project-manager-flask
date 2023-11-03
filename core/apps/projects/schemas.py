from core import marshmallow
from .models import Projects


class ProjectSchema(marshmallow.SQLAlchemyAutoSchema):
    """
    Serializer for the projects model.
    """

    class Meta:
        model = Projects
