from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = "postgres:12345@localhost:5432/postgres"
engine = create_engine(f'postgresql+psycopg2://{DATABASE_NAME}')
# dialect+driver://username:password@host:port/database
Session = sessionmaker(bind=engine)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(engine)