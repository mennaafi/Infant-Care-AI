from fastapi import APIRouter
from src.llm import get_response

chat_router = APIRouter(
    prefix="/api/v1",
    tags=["chat"],
)

@chat_router.get("/chat")
async def chat(query: str):
    response = get_response(query)
    return {"response": response}