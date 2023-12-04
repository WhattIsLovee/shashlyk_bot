from sqlalchemy import create_engine

from sqlalchemy.orm import Session, sessionmaker


import os
from dotenv import load_dotenv
load_dotenv()


engine = create_engine(os.getenv('DATABASE_URL'))
engine.connect()
session = Session(bind=engine)
