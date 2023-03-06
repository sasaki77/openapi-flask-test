import os

import connexion

from openapi_server import encoder
from openapi_server.config import DefaultSettings


def create_app():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.config.from_object('openapi_server.config.DefaultSettings')
    if "OPENAPISERVER_SETTINGS" in os.environ:
        app.app.config.from_envvar('OPENAPISERVER_SETTINGS')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Sample User API'},
                pythonic_params=True)

    return app, app.app
