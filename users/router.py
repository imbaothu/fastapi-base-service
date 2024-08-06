"""
User router : Register, login, logout and reset password
Reponse model : JWT Token with expiration time
"""

from fastapi import APIRouter, HTTPException
from users.schema import (
    UserLogin,
    UserRegistration,
    UserResetPassword,
)
from users.model import User, Role
from utils.security import hash_password, verify_password
from auth.jwt import create_access_token
from auth.payload import TokenData, Token

router = APIRouter()


@router.post("/register")
async def register_user(user_input: UserRegistration):
    """
    Register a new user
    """
    user = await User.find_by_email(user_input.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already exists")
    else:
        hashed_password = hash_password(user_input.password)
        user = User(
            **user_input.model_dump(exclude=("password")), password=hashed_password
        )
        await user.create()
        return user.model_dump(include=("username", "email", "role", "created"))


@router.post("/login")
async def login_user(user_input: UserLogin):
    """
    Login user
    """
    user = await User.find_by_email(user_input.email)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    if not verify_password(user_input.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    payload = TokenData(user_id=str(user.id), username=user.username, role=Role.MEMBER)
    access_token = create_access_token(payload.model_dump())
    return Token(access_token=access_token, token_type="bearer").model_dump()


@router.post("/logout")
async def logout_user():
    """
    Logout user
    """
    return {"message": "Logout successful"}


@router.post("/reset-password")
async def reset_password(user_input: UserResetPassword):
    """
    Reset user password
    """
    user: User = await User.find_by_email(user_input.email)
    if not user or verify_password(user_input.new_password, user.password):
        raise HTTPException(status_code=400, detail="User not found or wrong password")
    user.password = hash_password(user_input.new_password)
    await user.save()
    return user.model_dump(include=("username", "email", "role", "created"))


@router.get("/users")
async def get_users(page: int):
    """
    Get all users with pagination max = 10
    """
    total_users = await User.count()
    users = await User.find().skip(page * 10).limit(10).to_list()
    data = {
        "total_users": total_users,
        "users": [user.model_dump(include=("username", "email", "role", "created")) for user in users]
    }
    return data