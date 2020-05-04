from sqlalchemy import Column, Integer, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


engine = create_engine('sqlite:///opened_ads.db', echo=True)
Base = declarative_base()
_session_class = sessionmaker(bind=engine)
session = _session_class()


class OpenedAds(Base):
    __tablename__ = 'openedads'

    id = Column(Integer, primary_key=True)

    date_run = Column(Date)
    opened_ads = Column(Integer)

    # Lets us print out a user object conveniently.
    def __repr__(self):
        return "<User(date_run='%s', opened_ads='%i')>" % (
            self.date_run, self.opened_ads)


def create_db():
    Base.metadata.create_all(engine)


def create_ads_count():
    # Let's create a user and add two e-mail addresses to that user.
    opened_ads = OpenedAds(date_run=datetime.now(), opened_ads=0)
    session.add(opened_ads)
    session.commit()
    return opened_ads.id


def add_count(row_id):
    instance = session.query(OpenedAds).filter(OpenedAds.id == row_id).first()
    instance.opened_ads += 1
    session.commit()


def update_ads_count(row_id, opened_ads):
    instance = session.query(OpenedAds).filter(OpenedAds.id == row_id).first()
    instance.opened_ads = opened_ads
    session.commit()


def print_all_runs():
    runs = OpenedAds.query.all()
    for each in runs:
        print(f"Date: {each.date_run}, Count: {each.opened_ads}")


if __name__ == "__main__":
    create_db()
