from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from api import settings
from api.routes import auth, reservation, rooms, user


def create_app(test_config=None):
    #create app
    app=Flask(__name__, instance_relative_config=False)
    #importing the settings configuration
    app.config.from_pyfile('settings.py')
    #database configuration
    db = connect(**app.config['ME_CONNECT_OPTS'])
    app.config['primary_datastore'] = db[app.config['ME_CONNECT_OPTS']['db']]
    #cors config
    CORS(app, supports_credentials=True, resources={
        r"/api/*": {"origins": "*", 'expose_headers': settings.CORS_HEADERS},
    })
    #configure the rest endpoints - TODO
    #auth.configure(app)
    #reservation.configure(app)
    #rooms.configure(app)
    #user.configure(app)

    #run app in debug mode
    app.debug = app.config['FL_DEBUG']

    return app
