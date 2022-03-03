"""Subscription model."""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.schema import Table
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .. import Base

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
