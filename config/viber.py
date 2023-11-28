# Importing necessary modules from the viberbot package
from viberbot import Api, BotConfiguration

# Importing bot configuration values from a separate file
from values import BOT_NAME, AVATAR_URL, AUTH_TOKEN

# Creating an instance of the Viber API
# The configuration for the bot is provided from the imported values
viber = Api(BotConfiguration(name=BOT_NAME, avatar=AVATAR_URL, auth_token=AUTH_TOKEN))
