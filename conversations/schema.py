from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timezone

class ConversationInput(BaseModel):
    ai_model: str
    topic: Optional[str] = None
    new_message: str = None
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)