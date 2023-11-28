from interface.persistance.member import read_members, delete_member, add_member, read_member

from service.viber import send_user_message, send_admin_message, send_message_to_user_id


def handle_admin_message_request(viber_request):
    """
    Handles message requests from admin users.
    :param viber_request: The request object from Viber.
    """
    try:
        for member in read_members():
            send_user_message(member.id, viber_request.message, member.name)
        send_admin_message("")
    except Exception as e:
        send_admin_message(f"Failed to send message: {e}")

def handle_unsubscription(viber_request):
    """
    Handles unsubscription requests.
    :param viber_request: The request object from Viber.
    """
    user_id = viber_request.user_id
    try:
        delete_member(user_id)
        send_admin_message(f"{user_id} has been removed from DB")
    except Exception as e:
        send_admin_message(f"Remove Failed: {e}")

def handle_user_message(viber_request):
    """
    Handles messages from users.
    :param viber_request: The request object from Viber.
    """
    try:
        if not read_member(viber_request.sender.id):
            add_member(viber_request.sender.id, viber_request.sender.name)
            send_admin_message(f"{viber_request.sender.name} has been added to DB message= {viber_request.message.text}")
        else:
            send_admin_message(f"User {viber_request.sender.name} is sending message= {viber_request.message.text}")
            return
    except Exception as e:
        send_admin_message(str(e))

    welcome_message = (
        "Thank you for subscribing to PBS IT Club Bot.\n"
        "You will now receive alerts about events organized by IT Club.\n"
        "To unsubscribe:\n"
        "1. Open the bot.\n"
        "2. Tap on the 3-dots button in the top right and then on “Chat Info”\n"
        "3. Tap on 'Stop messages'\n"
        "Regards,\n"
        "PBS IT Club"
    )
    send_message_to_user_id(viber_request.sender.id, f"Hi {viber_request.sender.name}, {welcome_message}")

def handle_user_subscription(viber_request):
    """
    Handles subscription requests from users.
    :param viber_request: The request object from Viber.
    """
    try:
        add_member(viber_request.user.id, viber_request.user.name)
        send_admin_message(f"{viber_request.user.name} has subscribed")
        welcome_message = (
            "Thank you for subscribing to PBS IT Club Bot. "
            f"{viber_request.user.name}. You will now receive alerts "
            "about events organized by IT Club."
        )
        send_message_to_user_id(viber_request.user.id, welcome_message)
    except Exception as e:
        raise e
