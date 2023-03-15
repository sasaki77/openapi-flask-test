from openapi_server.handlers import get_users_handler


def test_get_users_handler(app):
    users = []
    with app.app_context():
        users = get_users_handler()
    assert len(users) == 3
