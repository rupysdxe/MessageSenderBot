from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()

class Member(Base):
    """
    SQLAlchemy model for a 'member' table.
    Each member has an id, a name, and a type.
    """
    # Table name in database
    __tablename__ = 'member'
    # Column definitions
    id = Column(Integer, primary_key=True)  # Unique identifier for each member
    name = Column(String, nullable=False)   # Name of the member, cannot be null
    type = Column(String, nullable=False)   # Type of the member, cannot be null
