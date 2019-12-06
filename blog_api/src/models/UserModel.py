# src/models/UserModel.py
from marshmallow import fields, Schema
#####################
# existing code remains #
########################
from .BlogpostModel import BlogpostSchema


class UserModel(db.Model):
    """
    User Model
    """

    # table name
    __tablename__ = 'users'

    #####################
    # existing code remains #
    ########################
    modified_at = db.Column(db.DateTime)
    blogposts = db.relationship('BlogpostModel', backref='users', lazy=True)  # add this new line

    #####################
    # existing code remains #
    ########################

    def __repr(self):
        return '<id {}>'.format(self.id)


# add this class
class UserSchema(Schema):
    """
    User Schema
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    blogposts = fields.Nested(BlogpostSchema, many=True)