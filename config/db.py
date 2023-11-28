# Import necessary library for database interaction
from sqlalchemy import create_engine

# Import database credentials from a separate file for security
from values import USER, PASSWORD, DATABASE_URL, DATABASE_NAME

# Construct the database connection string
# It's a good practice to use f-strings for improved readability and performance
config = f'mysql+pymysql://{USER}:{PASSWORD}@{DATABASE_URL}/{DATABASE_NAME}'

# Create an engine object to interact with the database
# This engine is the starting point for any SQLAlchemy application
engine = create_engine(config)
