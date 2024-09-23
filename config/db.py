from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'AT0jI5JHCZ74VXU86lmDFW1oY2QO9e3h'
MYSQL_HOST = 'fra1.clusters.zeabur.com'
MYSQL_PORT = '30923'
MYSQL_DATABASE = 'zeabur'
URL_DATABASE = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
