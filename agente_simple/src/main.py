import uvicorn
from fastapi import FastAPI

from src.routes.chat import router
from src.utils.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Agente Simple",
    description="Agente conversacional con LangChain create_agent, FastAPI y PostgreSQL.",
    version="1.0.0",
)

app.include_router(router)


if __name__ == "__main__":
    logger.info("Iniciando servidor en puerto 8080")
    uvicorn.run("src.main:app", host="0.0.0.0", port=8080, reload=False)
