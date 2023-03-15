import os

import connexion

from openapi_server import encoder
from openapi_server.database.database import init_db
from openapi_server.config import config


def create_app(config_name_=None):
    app = connexion.App(__name__, specification_dir='./openapi/')
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    if config_name_:
        config_name = config_name_
    app.app.config.from_object(config[config_name])
    if "OPENAPISERVER_SETTINGS" in os.environ:
        app.app.config.from_envvar('OPENAPISERVER_SETTINGS')
    app.app.json_encoder = encoder.JSONEncoder
    init_db(app.app)
    app.add_api('openapi.yaml',
                arguments={'title': 'Sample User API'},
                pythonic_params=True)

    return app.app
