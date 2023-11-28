from viberbot.api.messages import TextMessage

from config.viber import viber
from interface.persistance.member import read_admin_members, read_members


def send_user_message(u_id, msg, name):
    full_msg = '''Hi {f_name}, {body}'''.format(f_name=name, body=msg)
    viber.send_messages(to=u_id, messages=[TextMessage(text=full_msg)])

def send_message_to_user_id(u_id,message:str):
    viber.send_messages(to=u_id, messages=[TextMessage(text=message)])


def send_admin_message(msg):
    admin_members = read_admin_members()
    if admin_members is not None:
        for admin_member in admin_members:
            viber.send_messages(admin_member.id, messages=[TextMessage(text=msg)])


def send_message_to_members(msg):
    members = read_members()
    if members is not None:
        for member in members:
            viber.send_messages(member.id, messages=[TextMessage(text=msg)])

