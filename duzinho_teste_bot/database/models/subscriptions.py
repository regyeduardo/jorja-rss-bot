"""Subscription model."""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.schema import Table
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .. import Base

# class Subscription(Base):
#     __tablename__ = "subscriptions"

#     id = Column(Integer, primary_key=True, nullable=False)
#     created_at = Column(
#         TIMESTAMP(timezone=True),
#         nullable=False, server_default=text('now()'))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     feed_id = Column(Integer, ForeignKey('feeds.id'))

#     user = relationship(User, backref=backref("subscriptions", cascade="all, delete-orphan"))
#     product = relationship(Feed, backref=backref("subscriptions", cascade="all, delete-orphan"))

Subscription = Table(
    'subscriptions',
    Base.metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column(
        'created_at',
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text('now()'),
    ),
    Column('user_id', ForeignKey('users.id')),
    Column('feed_id', ForeignKey('feeds.id')),
)
