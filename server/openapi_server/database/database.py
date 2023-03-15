import click
from flask.cli import with_appcontext

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, downgrade, upgrade
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def init_db(app):
    import openapi_server.database.models

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    app.cli.add_command(mock_db_command)


@click.command("mock-db")
@with_appcontext
def mock_db_command():
    mock_db()


def mock_db():
    downgrade(revision="base")
    upgrade(revision="head")

    from openapi_server.database.models import User, Club

    users_dict = [
        {"name": "sasaki", "grade": 1, "club": ["Football", "Volleyball"]},
        {"name": "endo", "grade": 2, "club": ["Kendo", "Volleyball"]},
        {"name": "kaneko", "grade": 3, "club": ["Kendo", "Volleyball"]},
    ]

    for user in users_dict:
        u = User(name=user["name"], grade=user["grade"])
        for club in user["club"]:
            c = Club(club=club)
            u.club.append(c)
        db.session.add(u)
    db.session.commit()
