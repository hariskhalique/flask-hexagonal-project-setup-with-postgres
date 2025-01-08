import threading

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.config import appConfig
from flask_sqlalchemy import SQLAlchemy

class Database:
    """
    Thread-safe Singleton class for managing database engine, sessions, and ORM base.
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
                    cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """
        Initialize the database components.
        """
        self.engine = create_engine(appConfig.SQLALCHEMY_DATABASE_URI, echo=False)
        self.sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

# Flask-SQLAlchemy for Flask integration
db = SQLAlchemy()

# Singleton Instance
database = Database()

engine = database.engine
session = database.sessionLocal
