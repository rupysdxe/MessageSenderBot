from sqlalchemy.orm import sessionmaker

from config.db import engine
from models.member import Member


def add_member(member_id: int, name: str):
    """
    Adds a new member to the config.
    :param member_id: The ID of the member.
    :param name: The name of the member.
    """
    # Create a session
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Create a new member instance
        member = Member(id=member_id, name=name)
        # Add the new member to the session
        session.add(member)
        # Commit the transaction
        session.commit()

def delete_member(member_id: int):
    """
    Deletes a member from the config.

    :param member_id: The ID of the member to delete.
    """
    # Create a session
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Retrieve the member to be deleted
        member = session.query(Member).filter_by(id=member_id).first()
        if member:
            # Delete the member
            session.delete(member)
            # Commit the transaction
            session.commit()

def read_members()->list:
    """
    Retrieves all members from the config.

    :return: A list of Member instances.
    """
    # Create a session
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Query all members
        member_list = session.query(Member).all()
        # No need to commit for read-only operations
    return member_list

def read_member(member_id: str):
    """
    Retrieves a single member from the config.

    :param member_id: The ID of the member to retrieve.
    :return: A Member instance or None if not found.
    """
    # Create a session
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Retrieve a single member by ID
        member = session.query(Member).filter_by(id=member_id).first()
        # No need to commit for read-only operations
    return member


def read_admin_members():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Retrieve a single member by ID
        admin_members = session.query(Member).filter_by(type="ADMIN").all()
        # No need to commit for read-only operations
    return admin_members


def is_user_admin(user_id)->bool:
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Retrieve a single member by ID
        user = session.query(Member).filter_by(id=user_id).first()
        # No need to commit for read-only operations
    if user is not None:
        return True
    return False

