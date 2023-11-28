from viberbot.api.messages import TextMessage

from config.viber import viber
from interface.persistance.member import read_admin_members, read_members


def send_user_message(user_id, message, name):
    """
    Sends a personalized message to a specific user.
    :param user_id: ID of the user.
    :param message: Message content.
    :param name: Name of the user.
    """
    full_message = f"Hi {name}, {message}"
    viber.send_messages(to=user_id, messages=[TextMessage(text=full_message)])

def send_message_to_user_id(user_id, message: str):
    """
    Sends a message to a user specified by user ID.
    :param user_id: ID of the user.
    :param message: Message content.
    """
    viber.send_messages(to=user_id, messages=[TextMessage(text=message)])

def send_admin_message(message):
    """
    Sends a message to all admin members.
    :param message: Message content.
    """
    for admin_member in read_admin_members():
        viber.send_messages(admin_member.id, messages=[TextMessage(text=message)])

def send_message_to_members(message):
    """
    Sends a message to all members.
    :param message: Message content.
    """
    for member in read_members():
        viber.send_messages(member.id, messages=[TextMessage(text=message)])
