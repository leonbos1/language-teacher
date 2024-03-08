import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

url = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')

engine = create_engine(url)

Session = sessionmaker(bind=engine)

Base = declarative_base()

db = SQLAlchemy()
