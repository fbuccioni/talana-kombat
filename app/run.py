from fastapi import FastAPI

from .middleware import CORSOnAllMiddleware
from .routers import router

app = FastAPI(
    title="Talana Kombat",
    version="0.1.0",
    openapi_url="/api/v1/specs/openapi.json",
    docs_url="/api/v1/specs/swagger/",
    redoc_url="/api/v1/specs/redoc/"
)

origins = ['*']

app.include_router(router)
app.add_middleware(
    CORSOnAllMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
