from sqlalchemy import Column, Integer, String
from database import base


class User(base):
    __tablename__="users"
    # __table_args__={"schema":"training"}

    id = Column(Integer, primary_key= True, autoincrement= True, index= True )
    name = Column(String(100), index= True  )
    email = Column(String(100), unique= True, index= True )
    age = Column(Integer)



    # id = Column(Integer, primary_key= True, index= True)
    # name = Column(String(100), index= True)
    # email = Column(String(100), unique= True, index= True)
    # age = Column(Integer)
# class Student(base):
#     __tablename__="students"
#     __table_args__={"schema: training"}
#     id = Column(Integer, primary_key=True,autoincrement=True)
#     name = Column(String(50))


    
