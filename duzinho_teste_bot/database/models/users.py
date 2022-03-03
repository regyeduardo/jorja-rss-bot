"""Users model."""
from sqlalchemy import Column, String  # Integer
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy_utils import TimezoneType

from .. import Base


class User(Base):  # pylint: disable=too-few-public-methods
    """Users model."""

    __tablename__ = 'users'

    id = Column(String, primary_key=True, nullable=False)
    language = Column(String, nullable=False)
    timezone = Column(TimezoneType(backend='pytz'), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=text('now()')
    )
