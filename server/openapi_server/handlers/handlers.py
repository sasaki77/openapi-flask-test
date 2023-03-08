from flask import abort

from openapi_server.database.database import db
from openapi_server.database.models import User, Club

from openapi_server.models import User as U


def get_user_handler(name):
    stmt = db.select(User, Club.club).join(Club).where(User.name == name)
    result = db.session.execute(stmt)

    user = None
    club = []
    for i, row in enumerate(result):
        u, c = row
        if i == 0:
            user = u
        club.append(c)

    if user is None:
        abort(400, description=f"{name} doesn't exist in the database")

    return U(user.name, user.grade, club)


def get_users_handler():
    stmt = db.select(User, Club.club).join(Club)
    result = db.session.execute(stmt)

    users = {}
    for row in result:
        user, club = row
        if user.name not in users:
            users[user.name] = U(user.name, user.grade, [])
        users[user.name].clubs.append(club)

    return list(users.values())


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

    stmt = db.select(User, Club.club).join(Club).where(User.name == name)
    result = db.session.execute(stmt)

    user = None
    club = []
    for i, row in enumerate(result):
        u, c = row
        if i == 0:
            user = u
        club.append(c)

    if user is None:
        abort(400, description=f"{name} doesn't exist in the database")

    return U(user.name, user.grade, club), 201
