from beanie import Document, Indexed
from enum import Enum
from datetime import datetime, timezone

from beanie import Document
from pydantic import BaseModel
from typing import List
from datetime import datetime

# we don't save api key in the database


class AIModelEndpoint(Enum):
    OPENAI = "openai"
    GEMENI = "gemeni"


class Message(BaseModel):
    sender: str
    message: str
    is_highlighted: bool = False
    created_at: datetime = datetime.now(timezone.utc)


class Conversation(Document):
    user_id: str = Indexed()
    ai_model: AIModelEndpoint = Indexed()
    topic: str = Indexed()
    messages: List[Message]
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)
