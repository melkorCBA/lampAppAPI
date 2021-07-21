from flask import Flask
from data.db import initialize_db
from data.models import Lamp
from resources.lamp import lamps
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

# Connect to DB
try:
    initialize_db(app)
except:
    app.logger.error('Database Concetion failed')
app.register_blueprint(lamps)

app.run()
