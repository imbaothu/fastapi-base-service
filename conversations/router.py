"""
Conversations router: chat, react, highlight-noted, pin, delete, etc. 
auth required : jwt token

Follow standard JWT OAuth2.0 flow https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
"""

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from conversations.model import Conversation, Message
from conversations.schema import ConversationInput
from auth.jwt import oauth2_scheme, get_current_user
from endpoints import endpoint_manager
import json

router = APIRouter()


@router.post("/")
async def create_conversation(
    conversation_input: ConversationInput, token: str = Depends(oauth2_scheme)
):
    current_user = await get_current_user(token)
    print(current_user)
    if current_user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    new_mess = None
    if conversation_input.new_message is not None:
        new_mess = Message(
            sender=current_user.id_str, message=conversation_input.new_message
        )
    new_conversation = Conversation(
        user_id=current_user.id_str,
        ai_model=conversation_input.ai_model,
        topic=conversation_input.topic,
        messages=[new_mess] if new_mess is not None else [],
    )
    new_conversation = await new_conversation.create()

    # produce message to kafka
    await endpoint_manager.kafka_client.produce(my_topic="default", mess="minhdan")
    return {"message": "Message created successfully"}
