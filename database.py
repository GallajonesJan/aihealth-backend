#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker, declarative_base

#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://marinell:marinellendaya@localhost/ai_health_db"

#engine = create_engine(SQLALCHEMY_DATABASE_URL)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base = declarative_base()

#def get_db():
   # db = SessionLocal()
   # try:
    #    yield db
    #finally:
    #    db.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Railway MySQL connection (public network)
SQLALCHEMY_DATABASE_URL = (
    "mysql://root:BrNntmyGdyBODDsgNkJWoaOjoWEhOpkZ@tramway.proxy.rlwy.net:47575/railway"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

