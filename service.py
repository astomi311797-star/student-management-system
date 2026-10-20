from sqlalchemy.orm import Session
from repository import UserRepository
from schema import UserCreateRequest
from user import User

class UserService:
    def __init__(self):
        self.user_respository = UserRepository()
        

    def create_user(self,db:Session, user_payload: UserCreateRequest):
        user = User(name= user_payload.name, 
                     age= user_payload.age,
                    email= user_payload.email)
        self.user_respository.create_user(db, user)

    # def get_all_user(self, db:Session):
    #     return self.user_respository.get_all_user(db)

    def get_user_by_email(self, db:Session, email : str):
        self.user_respository.get_user_by_email(db, email)


    def delete_by_email_new(self, db:Session,email:str):
        self.user_respository.delete_by_email(db,email)
        return "Delete Successfully"


    
    # def delete_by_mail(self, db: Session, email: str):
    #     self.user_respositor.delete_by_email(db, email)
    #     return "delete succesfuuly"

