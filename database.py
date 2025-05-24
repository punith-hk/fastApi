from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
# SQLALCHEMY_DATABASE_URL =  "postgresql://postgres:punith%401903.@localhost/TodoApplicationDatabase"
SQLALCHEMY_DATABASE_URL = "postgresql://my_first_database_845y_user:G5zvg6k71cNBJvjjVjd1GTVNcqMkUF2R@dpg-d0otfm0dl3ps73aa5bo0-a.singapore-postgres.render.com/my_first_database_845y"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

