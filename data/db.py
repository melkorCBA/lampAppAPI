from flask_mongoengine import MongoEngine
import os 


db = MongoEngine()

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

def initialize_db(app):
    setConnection(app)
    db.init_app(app)

def setConnection(app):
    isConentionStringLoaded = len(str(os.getenv('MONGO_URI')[0:5]))
    if(isConentionStringLoaded < 5):
        app.logger.critical('Database Concetion string not loaded.')
        print("gfdgfgfd")
    else:
        app.logger.info('Database Concetion string loaded.')
        app.logger.info(str(os.getenv('MONGO_URI')[0:5]))
    
    app.config['MONGODB_SETTINGS'] = {
    'db': 'lamps',
    'host': os.getenv('MONGO_URI')
    }