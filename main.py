from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from core.config import settings
import urls
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME
)

static = FastAPI()

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
app.mount("/%s" % settings.PUBLIC_FOLDER,
          StaticFiles(directory=settings.PUBLIC_FOLDER),
          name=settings.PUBLIC_FOLDER)

if __name__ == "__main__":
    uvicorn.run("main:app", port=settings.PORT, host=settings.HOST, log_level="info")