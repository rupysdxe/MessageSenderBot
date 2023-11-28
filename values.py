import os

from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.environ.get('AUTH_KEY')
BACKEND_URL = os.environ.get('BACKED_URL')
BOT_NAME = os.environ.get('BOT_NAME')
AVATAR_URL=os.environ.get('AVATAR_URL')
DATABASE_URL = os.environ.get('DATABASE_URL')
USER=os.environ.get('DATABASE_USER')
DATABASE_NAME=os.environ.get('DATABASE_NAME')
PASSWORD=os.environ.get('DATABASE_PASSWORD')

