from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Hello World!111111222555'


if __name__ == '__main__':
    application.run()
