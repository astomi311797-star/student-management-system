from fastapi import APIRouter, Depends, status
from schema import UserCreateRequest
from database import get_db
from service import UserService
from sqlalchemy.orm import Session

router = APIRouter(
prefix="/user"
)

@router.post("/create")
def create_user(user_payload : UserCreateRequest, db: Session = Depends(get_db)):
    user_service = UserService()
    user_service.create_user(db, user_payload)

# @router.get("/list")
# def get_all_user( db: Session = Depends(get_db)):
#     service = UserService()
#     return service.get_all_user(db)


@router.get("/{email}")
def get_user_by_email_new(email:str, db:Session = Depends(get_db)):
    service = UserService()
    return service.get_user_by_email(db, email)

@router.delete("/{email}")
def delete_by_email_Conto(email:str, db:Session = Depends(get_db)):
    service_New = UserService()
    return service_New.delete_by_email_new(db,email)




# @router.delete("/{email}")
# def delete_user_by_email(email:str, db:Session = Depends(get_db)):
#     service = UserService()
#     return service.get_user_by_email(db, email)