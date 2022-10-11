from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextvars import ContextVar
from sqlalchemy.orm import Session
from sqlalchemy.engine.mock import MockConnection

# db_context hold different session for each request
db_context_var: ContextVar[Session] = ContextVar('db')
db_context_engine: ContextVar[MockConnection] = ContextVar('db_engine')
Base = declarative_base()


def _create_engine():

    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:tu1den10@localhost:5432/postgres"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, pool_timeout = 60
    )

   # create engine
    return engine


def create_db():
   """Create db connection"""
   engine = db_engine
   
   session_local = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False)
   session_local.configure(binds={
      Base: engine
   })
   return session_local()


def get_engine():
   if db_context_engine.get(None) is None:
      db_context_engine.set(_create_engine())
   return db_context_engine.get()


class _DBEngine:
   def __getattr__(self, item):
      return getattr(get_engine(), item)

   def __setattr__(self, key, value):
      return setattr(get_engine(), key, value)


def get_db():
   if db_context_var.get(None) is None:
      db_context_var.set(create_db())
   return db_context_var.get()


class _DBProxy:
   def __getattr__(self, item):
      return getattr(get_db(), item)

   def __setattr__(self, key, value):
      return setattr(get_db(), key, value)


db_engine = _DBEngine()
db = _DBProxy()