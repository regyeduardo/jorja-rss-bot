"""Database settings."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from duzinho_teste_bot import get_database_connection

DB_URL = get_database_connection()
engine = create_engine(
    DB_URL, echo=True, #pool_size=5, max_overflow=0, pool_pre_ping=True, pool_use_lifo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
