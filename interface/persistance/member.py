from sqlalchemy.orm import sessionmaker

from config.db import engine
from models.member import Member

# Create a session factory, this is more efficient than creating it inside every function
Session = sessionmaker(bind=engine)

def add_member(member_id: int, name: str):
    """
    Adds a new member to the database.
    :param member_id: The ID of the member.
    :param name: The name of the member.
    """
    with Session() as session:
        member = Member(id=member_id, name=name)
        session.add(member)
        session.commit()

def delete_member(member_id: int):
    """
    Deletes a member from the database.
    :param member_id: The ID of the member to delete.
    """
    with Session() as session:
        member = session.query(Member).filter_by(id=member_id).first()
        if member:
            session.delete(member)
            session.commit()

def read_members() -> list:
    """
    Retrieves all members from the database.
    :return: A list of Member instances.
    """
    with Session() as session:
        return session.query(Member).all()

def read_member(member_id: int):
    """
    Retrieves a single member from the database.
    :param member_id: The ID of the member to retrieve.
    :return: A Member instance or None if not found.
    """
    with Session() as session:
        return session.query(Member).filter_by(id=member_id).first()

def read_admin_members() -> list:
    """
    Retrieves all admin members from the database.
    :return: A list of admin Member instances.
    """
    with Session() as session:
        return session.query(Member).filter_by(type="ADMIN").all()

def is_user_admin(user_id: int) -> bool:
    """
    Checks if a user is an admin.
    :param user_id: The ID of the user.
    :return: True if the user is an admin, False otherwise.
    """
    with Session() as session:
        user = session.query(Member).filter_by(id=user_id).first()
        return user is not None and user.type == "ADMIN"
