from sqlalchemy import Column, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime


Base = declarative_base()


class OpenedAds(Base):
    __tablename__ = 'openedads'

    id = Column(Integer, primary_key=True)

    date_run = Column(DateTime, default=datetime.now)
    opened_ads = Column(Integer, default=0)
    failed = Column(Integer, default=0)

    # Lets us print out a user object conveniently.
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Date: {self.formatted_date()} - Count: {self.opened_ads} - Failed: {self.failed}"

    def formatted_date(self):
        return self.date_run.strftime("%Y-%B-%a-%H:%Mhs")


def get_engine():
    return create_engine('sqlite:///opened_ads.db', echo=False)


def get_session():
    session_factory = sessionmaker(bind=get_engine())
    session_class = scoped_session(session_factory)
    return session_class(), session_class


def create_db():
    Base.metadata.create_all(get_engine())


def create_ads_count():
    session, session_class = get_session()
    # Let's create a user and add two e-mail addresses to that user.
    opened_ads = OpenedAds(date_run=datetime.now())
    session.add(opened_ads)
    session.commit()
    aux_id = opened_ads.id
    session_class.remove()
    return aux_id


def add_count(row_id):
    session, session_class = get_session()
    instance = session.query(OpenedAds).filter(OpenedAds.id == row_id).first()
    instance.opened_ads += 1
    session.commit()
    session_class.remove()


def add_failed(row_id):
    session, session_class = get_session()
    instance = session.query(OpenedAds).filter(OpenedAds.id == row_id).first()
    instance.failed += 1
    session.commit()
    session_class.remove()


def update_ads_count(row_id, opened_ads):
    session, session_class = get_session()
    instance = session.query(OpenedAds).filter(OpenedAds.id == row_id).first()
    instance.opened_ads = opened_ads
    session.commit()
    session_class.remove()


def update_failed_count(row_id, failed):
    session, session_class = get_session()
    instance = session.query(OpenedAds).filter(OpenedAds.id == row_id).first()
    instance.failed = failed
    session.commit()
    session_class.remove()


def print_all_runs():
    session, session_class = get_session()
    runs = session.query(OpenedAds).all()
    for each in runs:
        print(each)
    session_class.remove()


if __name__ == "__main__":
    create_db()
