import flask
from telebot import types
# from config import *
# from bot_handlers import bot
import os

server = flask.Flask(__name__)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
