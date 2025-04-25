from fastapi import APIRouter
from pydantic import BaseModel
from src.llm import get_response

chat_router = APIRouter(
    prefix="/api/v1",
    tags=["chat"],
)

class ChatRequest(BaseModel):
    query: str

@chat_router.post("/chat")
async def chat(request: ChatRequest):
    response = get_response(request.query)
    return {"response": response}