# config.py
import os


MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = '3310'
MYSQL_USER = 'myuser'
MYSQL_PASSWORD = 'mypassword'
MYSQL_DATABASE = 'mydatabase'
# config.py
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
