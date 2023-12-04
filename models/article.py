from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    link = Column(String(100), nullable=False)
    title = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    #favorites = relationship("Favorite")