from fastapi import FastAPI
from starlette.requests import Request
import uvicorn
import logging

from app.utils import config
from app.presentation.api_v1.cars import cars_router

# Configure basic config of logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='./logs/ApiLogs.log',
                    filemode='w')

app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = await call_next(request)
    return response


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}

app.include_router(
    cars_router,
    prefix="/api/v1",
    tags=["cars"],
)

# Routers
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)

