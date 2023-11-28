import logging

from flask import request, Response
from interface.persistence.member import is_user_admin
from viberbot.api.viber_requests import ViberMessageRequest, ViberSubscribedRequest, ViberUnsubscribedRequest

from config.viber import viber
from service.request_event_handler import (
    handle_admin_message_request,
    handle_user_message,
    handle_user_subscription,
    handle_unsubscription
)


def handle_viber_request():
    """
    Handles incoming requests from Viber and dispatches them based on their type.
    """
    viber_request = viber.parse_request(request.get_data())
    logging.info("Request from viber: %s", viber_request)

    # Verify the Viber request signature
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # Handle different types of Viber requests
    if isinstance(viber_request, ViberMessageRequest):
        if is_user_admin(viber_request.sender.id):
            handle_admin_message_request(viber_request)
        else:
            handle_user_message(viber_request)

    elif isinstance(viber_request, ViberSubscribedRequest):
        handle_user_subscription(viber_request)

    elif isinstance(viber_request, ViberUnsubscribedRequest):
        handle_unsubscription(viber_request)

    return Response(status=200)
