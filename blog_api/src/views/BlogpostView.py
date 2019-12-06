# /src/views/BlogpostView.py
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


@blogpost_api.route('/<int:blogpost_id>', methods=['PUT'])
@Auth.auth_required
def update(blogpost_id):
    """
  Update A Blogpost
  """
    req_data = request.get_json()
    post = BlogpostModel.get_one_blogpost(blogpost_id)
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = blogpost_schema.dump(post).data
    if data.get('owner_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    data, error = blogpost_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)
    post.update(data)

    data = blogpost_schema.dump(post).data
    return custom_response(data, 200)