# src/models/BlogpostModel.py
#####################
# existing code remains #
########################
from marshmallow import fields, Schema

class BlogpostModel(db.Model):
  """
  Blogpost Model
  """

  __tablename__ = 'blogposts'

  #####################
  # existing code remains #
  ########################
  contents = db.Column(db.Text, nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # add this new line
  #####################
  # existing code remains #
  ########################

  def __init__(self, data):
    #####################
    # existing code remains #
    ########################
    self.owner_id = data.get('owner_id) # add this new line
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  #####################
  # existing code remains #
  ########################

  def __repr__(self):
    return '<id {}>'.format(self.id)

# add this new class
class BlogpostSchema(Schema):
  """
  Blogpost Schema
  """
  id = fields.Int(dump_only=True)
  title = fields.Str(required=True)
  contents = fields.Str(required=True)
  owner_id = fields.Int(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)