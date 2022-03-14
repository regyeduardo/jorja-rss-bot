from duzinho_teste_bot.database import Subscription, engine, User, SessionLocal
from sqlalchemy import Column, String
import feedparser
# from duzinho_teste_bot.utils.tasks import check_subs

def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))

# column = Column('title', String, nullable=True)
# add_column(engine, 'subscriptions', column)

def insert_title():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    for user in users:
        session = SessionLocal()
        subs = (
            session.query(Subscription)
            .filter(Subscription.user_id == user.id)
            .all()
        )
        session.close()
        if subs:
            for sub in subs:
                if not sub.title:
                    session = SessionLocal()
                    db_sub = session.query(Subscription).filter(Subscription.id == sub.id).first()
                    feed = feedparser.parse(sub.url)
                    title = feed.feed.title
                    db_sub.title = title
                    session.add(db_sub)
                    session.commit()
                    session.close()

# insert_title()

# engine.execute('ALTER TABLE subscriptions ADD CONSTRAINT url_unique UNIQUE (url)'
# engine.execute('ALTER TABLE subscriptions DROP CONSTRAINT url_unique')