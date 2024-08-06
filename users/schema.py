"""
User schemas  - Pydantic models for user registration, login and update
User registration schema
User login schema
User update schema
"""

from pydantic import BaseModel, EmailStr, Field

class UserRegistration(BaseModel):
    """
    User registration schema
    """
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

class UserLogin(BaseModel):
    """
    User login schema
    """
    email: EmailStr = Field(...)
    password: str = Field(...)

class UserResetPassword(BaseModel):
    """
    User reset password schema
    """
    email: EmailStr = Field(...)
    password: str = Field(...)
    new_password: str = Field(...)
