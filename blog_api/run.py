# /run.py
import os

from src.app import create_app


def set_environment_variables():

    os.environ["FLASK_ENV"] = "development"
    os.environ["DATABASE_URL"] = 'postgres://name:password@houst:port/blog_api_db'
    os.environ["JWT_SECRET_KEY"] = 'hhgaghhgsdhdhdd'


if __name__ == '__main__':
    set_environment_variables()

    env_name = os.getenv('FLASK_ENV')

    if env_name is None:
        env_name = 'Development'

    app = create_app(env_name)
    # run app
    app.run()