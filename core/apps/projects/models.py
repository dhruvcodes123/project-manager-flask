from core import db
from datetime import datetime


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    @classmethod
    def save(cls, data):
        """
        Creates and saves model object.
        Parameter:
        data: Python Dictionary
            key refers to the attribute of models.
        Return:
            model object
        """
        project = cls(
            title=data.get('title'),
            description=data.get('description'),
            completed=data.get('completed', False)
        )
        db.session.add(project)
        db.session.commit()
        return project
