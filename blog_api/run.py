# /run.py
import os

from src.app import create_app

env_name = os.getenv('FLASK_ENV')

if __name__ == '__main__':
  port = os.getenv('PORT')
