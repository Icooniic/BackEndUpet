from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'ejemplo'
#mysqlsh --sql --host=fra1.clusters.zeabur.com --port=30809 --user=root --password=zSAit7Lyd8xKh3og96aJ5EPDOe40w12v --schema=zeabur
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
