"""Feed model."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy_utils import URLType

from .. import Base


class Feed(Base):
    """Feed model."""

    __tablename__ = 'feeds'
    # pylint: disable=too-few-public-methods

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    url = Column(URLType, nullable=False)
    icon = Column(URLType, nullable=True)
    datetime_last_post = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')
    )
