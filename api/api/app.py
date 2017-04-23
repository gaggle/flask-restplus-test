import logging

from flask import Flask
from versioned_api import Api


def main():
    app = Flask(__name__)
    Api(app, {1: 'v1'})
    app.run(debug=DEBUG)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    DEBUG = True
    main()
