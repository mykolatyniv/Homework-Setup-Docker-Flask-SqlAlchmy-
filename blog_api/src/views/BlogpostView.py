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

# add this function
@blogpost_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Blogposts
  """
  posts = BlogpostModel.get_all_blogposts()
  data = blogpost_schema.dump(posts, many=True).data
  return custom_response(data, 200)


# app initiliazation
#####################
# existing code remain #
######################