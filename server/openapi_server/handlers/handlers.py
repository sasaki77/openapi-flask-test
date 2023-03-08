from flask import abort
from sqlalchemy.orm import contains_eager

from openapi_server.database.database import db
from openapi_server.database.models import User, Club
from openapi_server.database.models import user_schema, users_schema


def get_user_handler(name):
    stmt = (
        db.select(User)
        .join(User.club)
        .options(contains_eager(User.club))
        .where(User.name == name)
    )

    user = db.session.scalars(stmt).unique().first()

    if user is None:
        abort(400, description=f"{name} doesn't exist in the database")

    return user_schema.dump(user)


def get_users_handler():
    stmt = db.select(User).join(User.club).options(contains_eager(User.club))
    result = db.session.scalars(stmt).unique()

    users = [row for row in result]

    return users_schema.dump(users)


def post_user_handler(name, user):
    if name != user.name:
        abort(
            400,
            description=f"The name in the path is different from the name in the body",
        )

    u = User(name=name, grade=user.grade)
    c = []
    if user.clubs is not None:
        for club in user.clubs:
            c.append(Club(club=club))
    u.club = c
    db.session.add(u)
    db.session.commit()

    stmt = (
        db.select(User)
        .join(User.club)
        .where(User.name == name)
        .options(contains_eager(User.club))
    )

    user = db.session.scalars(stmt).unique().first()

    if user is None:
        abort(400, description=f"{name} doesn't exist in the database")

    return user_schema.dump(user), 201
