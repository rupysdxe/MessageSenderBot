# ViberBot
This was a small Viber BOT project implemented in Python with the Flask framework to make webhooks 
that can be called by the Viber server if users interacted with Viber bot.

<h4>Tech :</h4>
1. MySQL 
2. Python - Flask


<h4>Features:</h4>

1. Can send multiple messages to all Viber users who have subscribed to the bot at once.

2. Messages can be sent to multiple subscribers by sending them directly to the Viber Bot only from the admin Viber account.

3. Messages sent to Viber Bot from users are routed directly to the ADMIN Viber account.

4. Event information, such as unsubscriptions, subscriptions, and messages sent to BOT, is directly sent to Admin  Viber account.

## Project Structure
- `config`: Configuration files and settings.
- `interface`: User interface components.
- `models`: Data models and business logic.
- `service`: Service layer for handling business logic.
- `app.py`: Main application file.
- `requirements.txt`: List of project dependencies.
- `Dockerfile`: Docker configuration for containerization.
- `values.py`: Additional configuration values.

## Installation and Setup

Docker is required.

To to project root direcotry and run

```bash
docker build -t viberbot .
```

After image is created run 

```bash
docker run -d -p 5000:5000 --name bot --restart always --env-file .env viberbot
```


<h4>Demo Images: </h4>

<a href="url"><img src="https://github.com/rupysdxe/ViberBot/blob/main/demo/IMG_0850.PNG" width="300" height="650"></a>
<a href="url"><img src="https://github.com/rupysdxe/ViberBot/blob/main/demo/IMG_0851.PNG" width="300" height="650"></a>
<a href="url"><img src="https://github.com/rupysdxe/ViberBot/blob/main/demo/IMG_0852.PNG" width="300" height="650"></a>
<a href="url"><img src="https://github.com/rupysdxe/ViberBot/blob/main/demo/IMG_0853.PNG" width="300" height="650"></a>
