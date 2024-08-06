from beanie import Document, Indexed
from datetime import datetime, timezone
from typing import Optional
from pydantic import Field
from enum import Enum
from bson import ObjectId


class Role(str, Enum):
    MEMBER = "member"
    ADMIN = "admin"
    GUEST = "guest"


class User(Document):
    """
    User DB representation
    """

    username: str = Indexed(unique=True)
    email: str = Indexed(unique=True)
    password: str
    role: Role = Field(default=Role.MEMBER)
    is_active: bool = Field(default=False)

    updated_at: datetime = datetime.now(timezone.utc)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def created(self) -> datetime | None:
        """Datetime user was created from ID."""
        return self.id.generation_time if self.id else None

    @classmethod
    async def find_by_email(cls, email: str) -> Optional["User"]:
        """Get a user by email."""
        return await cls.find_one(cls.email == email)
    
    @classmethod
    async def find_by_id(cls, user_id: str) -> Optional["User"]:
        """Get a user by id."""
        return await cls.find_one(cls.id == ObjectId(user_id))
    
    @property
    def id_str(self) -> str:
        """Get user id as string."""
        return str(self.id)
