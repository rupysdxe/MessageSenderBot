from flask import Flask

from interface.rest.viber_request import handle_viber_request

# Create a flask app
app = Flask(__name__)




# Routes
app.route('/', methods=['POST'])(handle_viber_request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


