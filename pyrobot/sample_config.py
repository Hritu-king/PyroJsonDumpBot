import os


class Config:
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6181365570:AAEklmfU6eifF4wQt9EgueVI5tM0zDVHHRQ")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 29616312))
    API_HASH = os.environ.get("API_HASH", "dd1a05ab4c47a5a037cc067cf4bded27")
