# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy import func

from app import DeclarativeBase

# Define a base model for other database tables to inherit
class Base(DeclarativeBase):

    __abstract__  = True

    id            = Column(Integer, primary_key=True)
    date_created  = Column(DateTime,  default=func.current_timestamp())
    date_modified = Column(DateTime,  default=func.current_timestamp(),
                                        onupdate=func.current_timestamp())


# Define a User model
class Account(Base):

    __tablename__ = 'auth_user'

    email        = Column(String(128),  nullable=False, unique=False)
    password     = Column(String(192),  nullable=False)
    shortname    = Column(String(128),  nullable=False, unique=True)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.shortname = shortname
        self.email = email
        self.password = password

    def __repr__(self):
        return '<account %r>' % (self.shortname)