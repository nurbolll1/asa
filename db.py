from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Notification_db(Base):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True)
    url_img = Column(String)
    text = Column(String)

engine = create_engine('sqlite:///notification.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


