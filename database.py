from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



 
# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"

DATABASE_URL = "postgresql+psycopg2://training_g5ys_user:SrEUvZpt4IlwYG2AFZ7olKhm6vZrnDrL@dpg-dbbfgne7bikc738cutvg-a.oregon-postgres.render.com/training_g5ys"

engine = create_engine(DATABASE_URL)
localSession = sessionmaker(autocommit = False, autoflush = False,bind =engine)
base = declarative_base() 

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close