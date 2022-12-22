import os

from dotenv import load_dotenv
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
#Переменные окружения из файла env
DATABASE = os.getenv('NAME_DB'),
USER = os.getenv('USER'),
PASSWORD = os.getenv('PASSWORD'),
HOST = os.getenv('HOST'),
PORT = os.getenv('PORT')


Base = declarative_base()
engine = create_engine(
    f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
)

# Таблица Пользователя в БД
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False, index=True)
    name = Column(String)

# Таблица Голосовых в БД
class Voice(Base):
    __tablename__ = 'audio_message'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey(User.user_id))
    message_id = Column(Integer)
    audio_path = Column(String)

# Таблица Фото в БД
class Photo(Base):
    __tablename__ = 'photo_message'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey(User.user_id))
    message_id = Column(Integer)
    photo_path = Column(String)


Base.metadata.create_all(engine)
Sessia = sessionmaker(bind=engine)
sessia = Sessia()
