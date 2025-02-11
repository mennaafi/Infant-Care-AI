from fastapi import FastAPI
from src.routes import base, chat 

app = FastAPI()

app.include_router(base.base_router)
app.include_router(chat.chat_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)