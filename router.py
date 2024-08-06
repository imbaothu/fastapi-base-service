"""
Router package
"""

from fastapi import APIRouter
from users.router import router as user_router
from conversations.router import router as conversation_router
from example.router import router as example_router

router = APIRouter(prefix="/api/v1")
router.include_router(user_router, tags=["users"], prefix="/users")
router.include_router(conversation_router, tags=["conversation"], prefix="/conversations")
router.include_router(example_router, tags=["example websocket"], prefix="/example") # for demo SSE, WS
