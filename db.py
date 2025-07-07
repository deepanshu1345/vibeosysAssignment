from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DB_URL = "postgresql://deepanshulakde:Deepu26@localhost:5432/test"
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit = False)
Base = declarative_base()
