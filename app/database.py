from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
# SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:password@localhost/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# print(SQLALCHEMY_DATABASE_URL)
#used to create an Engine object, which represents a connection to a database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#create a Session class with specific configurations for managing database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#used to create a base class for declarative class definitions, allowing you to define database models using a declarative syntax
Base = declarative_base()

# used to create a session to our database everytime we get a request to API endpoint and later closes it out
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi', user='postgres', 
#                                 password='password', cursor_factory=RealDictCursor)
    
#         cursor = conn.cursor()
#         print("Database connection successful")
#         break
#     except Exception as err:
#         print("Connecting to DB failed")
#         print(f"Err was {err}")
#         time.sleep(2)