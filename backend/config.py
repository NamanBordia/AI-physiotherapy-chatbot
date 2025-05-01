import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "Naman@123")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "Naman@935106")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "mysql+pymysql://root:Naman%40123@localhost/ai_physio_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress a warning
    BIOBERT_MODEL_PATH = os.getenv("BIOBERT_MODEL_PATH", "models/biobert")
