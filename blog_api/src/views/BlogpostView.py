#/src/views/BlogpostView.py
# app initiliazation
#####################
# existing code remain #
######################


@blogpost_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Blogpost Function
  """
  # app initiliazation
  #####################
  # existing code remain #
  ######################
  return custom_response(data, 201)

# app initiliazation
#####################
# existing code remain #
######################


@blogpost_api.route('/<int:blogpost_id>', methods=['DELETE'])
@Auth.auth_required
def delete(blogpost_id):
  """
  Delete A Blogpost
  """
  post = BlogpostModel.get_one_blogpost(blogpost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = blogpost_schema.dump(post).data
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  post.delete()
  return custom_response({'message': 'deleted'}, 204)