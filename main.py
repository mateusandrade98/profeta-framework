from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config import settings
from core.routes import routeStatic
import urls
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME
)

if len(settings.BACKEND_CORS_ORIGINS):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# routers: views/
app.include_router(urls.Router())

# public folder
app.include_router(routeStatic)

if __name__ == "__main__":
    uvicorn.run("main:app", port=settings.PORT, host=settings.HOST, log_level="info")