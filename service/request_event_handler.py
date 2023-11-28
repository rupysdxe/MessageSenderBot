from interface.persistance.member import read_members, delete_member, add_member, read_member
from service.viber import send_user_message, send_admin_message, send_message_to_user_id


def handle_admin_message_request(viber_request):
    try:
      mem_list = read_members()
      for member in mem_list:
          f_name = member.name
          member_id =member.id
          send_user_message(member_id, viber_request.message, f_name)
          send_admin_message("")
    except Exception as e:
        send_admin_message("Failed to send message")


def handle_unsubscription(viber_request):
    user_id = viber_request.user_id
    try:
        delete_member(user_id)
        send_admin_message(str(viber_request.user_id) + " has been removed from DB")
    except Exception as e:
        send_admin_message("Remove Failed")


def handle_user_message(viber_request):
    try:
        res = read_member(viber_request.sender.id)
        if res is None:
            add_member(viber_request.sender.id,viber_request.sender.name)
            send_admin_message(str(viber_request.sender.name) + ' has been added to DB message= ' + str(viber_request.message.text))
        else:
            send_admin_message(
                'User ' + str(viber_request.sender.name) + " is sending message= " + str(viber_request.message.text))
            return
    except Exception as e:
        send_admin_message(str(e))
    mes = '''
    Thank you for subscribing to PBS IT Club Bot.
    You will now receive alerts about events organized by IT Club.
    To unsubscribe:
    1. Open the bot.
    2. Tap on the 3-dots button in the top right and then on “Chat Info”
    3. Tap on "Stop messages"
    Regards,
    PBS IT Club
    '''
    send_message_to_user_id(viber_request.sender.id,"Hi " + str(viber_request.sender.name) + "," + mes)


def handle_user_subscription(viber_request):
    try:
        add_member(viber_request.user.id,viber_request.user.name)
        send_admin_message(str(viber_request.user.name + " has subscribed"))
        send_message_to_user_id(viber_request.user.id, message='Thank you for subscribing to PBS IT Club Bot. ' + str(
            viber_request.user.name) + '. You will now '
                                       'receive alerts '
                                       'about events '
                                       'organized by '
                                       'IT Club.')
    except Exception as e:
        raise e




