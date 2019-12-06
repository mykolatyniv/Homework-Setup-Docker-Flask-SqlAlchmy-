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

@blogpost_api.route('/<int:blogpost_id>', methods=['GET'])
def get_one(blogpost_id):
  """
  Get A Blogpost
  """
  post = BlogpostModel.get_one_blogpost(blogpost_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = blogpost_schema.dump(post).data
  return custom_response(data, 200)


# app initiliazation
#####################
# existing code remain #
######################