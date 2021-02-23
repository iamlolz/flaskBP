# basic setup
from flask import Flask
from config import Config

# create application object
app = Flask(__name__)
app.config.from_object(Config)

# import views
from app import views


if __name__ == "__main__":
    app.run(host='0.0.0.0')
