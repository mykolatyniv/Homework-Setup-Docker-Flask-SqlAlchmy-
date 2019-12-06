# src/app.py

from flask import Flask

from .config import app_config
from .models import db, bcrypt

# import user_api blueprint
from .views.UserView import user_api as user_blueprint  # add this line


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    #####################
    # existing code remain #
    ######################

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')  # add this line

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your first endpoint is working'

    return app
