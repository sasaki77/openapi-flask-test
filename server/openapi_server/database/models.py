from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import ForeignKey
from openapi_server.database.database import db


class User(db.Model):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String(80), primary_key=True)
    grade: Mapped[int]

    club: Mapped[List["Club"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(name={self.name!r}, grade={self.grade!r})"


class Club(db.Model):
    __tablename__ = "club"

    name = mapped_column(ForeignKey("user.name"), primary_key=True)
    club: Mapped[str] = mapped_column(String(20), primary_key=True)

    user: Mapped[User] = relationship(back_populates="club")

    def __repr__(self) -> str:
        return f"Address(name={self.name!r}, club={self.club!r})"
