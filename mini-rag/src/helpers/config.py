from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    MODEL_NAME: str
    EMBEDDING_MODEL_NAME: str
    MODEL_API_KEY: str
    
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME: str


    class Config:
        env_file = ".env"

def get_settings():
    return Settings()