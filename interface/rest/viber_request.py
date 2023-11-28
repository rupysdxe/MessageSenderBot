import logging

from flask import request, Response
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

from config.viber import viber
from interface.persistance.member import is_user_admin
from service.request_event_handler import handle_admin_message_request, handle_user_message, handle_user_subscription, \
    handle_unsubscription


def handle_viber_request():
    viber_request = viber.parse_request(request.get_data())
    logging.log(logging.INFO,"Request from viber: ",viber_request)
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)
    if isinstance(viber_request, ViberMessageRequest):
        if is_user_admin(viber_request.sender.id):
            handle_admin_message_request(viber_request)
        else:
            handle_user_message(viber_request)
    if isinstance(viber_request, ViberSubscribedRequest):
        handle_user_subscription(viber_request)
    if isinstance(viber_request, ViberUnsubscribedRequest):
        handle_unsubscription(viber_request)
    return Response(status=200)

