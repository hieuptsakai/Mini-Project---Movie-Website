from operator import mod
from fastapi import APIRouter
from models.user import UserModel
router = APIRouter()
        

@router.get("/api/users")
def get_users(user_code: str):
    return UserModel.get_user_by_user_code(user_code)

