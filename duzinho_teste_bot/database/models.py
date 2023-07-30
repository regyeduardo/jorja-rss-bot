"""Database tables."""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy_utils import TimezoneType, URLType

from . import Base


class User(Base):  # pylint: disable=too-few-public-methods
    """User table model.

    Args:
        Base (Base): Base model.
    """

    __tablename__ = 'users'

    id = Column(String(255), primary_key=True, nullable=False)
    language = Column(String(255), nullable=False)
    timezone = Column(TimezoneType(backend='pytz'), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=text('now()')
    )
    subscriptions = relationship('Subscription', back_populates='user')


class Subscription(Base):
    """User's feeds.

    Args:
        Base (any): Base model.

    Returns:
        Subscription: Iterator for user's subscriptions
    """

    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    url = Column(URLType, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text('now()'),
    )
    datetime_last_post = Column(TIMESTAMP(timezone=False), nullable=True)
    user_id = Column(String(255), ForeignKey('users.id'))
    user = relationship('User', back_populates='subscriptions')

    def __getitem__(self, item):
        """_summary_

        Args:
            item (User): An unique user.

        Returns:
            any: An user.
        """
        return self.user_id[item]
