import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

JWT_SECRET_KEY = os.getenv('SECRET_KEY') or "teste123"