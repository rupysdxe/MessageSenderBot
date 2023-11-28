from viberbot import Api, BotConfiguration

from values import BOT_NAME, AVATAR_URL, AUTH_TOKEN

viber: Api= Api(BotConfiguration(
    name=BOT_NAME,
    avatar=AVATAR_URL,
    auth_token=AUTH_TOKEN
))






