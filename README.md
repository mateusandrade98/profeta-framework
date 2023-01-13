# Profeta-Framework
Prophet-framework is based on [FastAPI](https://github.com/tiangolo/fastapi) and has an architecture similar to [Django](https://www.djangoproject.com/).

This framework emerged from the need for high-performance Dashboards and real-time APIs.

In addition to the MVC (Model-View-Controller) architecture, Prophet-framework uses [MongoDB](https://www.mongodb.com/) as a NoSQL database.

**Prophet-Framework** is a great tool for those looking for high performance and a simple architecture to work with.

### Creating an app
```python manager.py startapp newapp```

### Architecture

Files responsible for Controls ``controllers/``

Files responsible for Views ``views/``

Files responsible for Templates HTML ``templates/``

Folder with public files ``public/``

### Settings
core/config.py

```
PROJECT_NAME: str = "project name"
PORT: int = 8005
HOST: str = '0.0.0.0'
SECRET_KEY: str = secrets.token_urlsafe(32)
MONGO_CONNECTION_STRING: str = 'mongodb://docker:mongopw@localhost:55000'
MONGO_COLLECTIONS: str = 'users'
MONGO_DATABASE: str = 'myFirstDatabase'
FIRST_SUPERUSER_NAME: str = 'dev'
FIRST_SUPERUSER_EMAIL: str = 'me@example.com'
FIRST_SUPERUSER_PASSWORD: str = 'dev'
BACKEND_CORS_ORIGINS: list = []
PUBLIC_FOLDER: str = 'public'
```

### Routes
To manage them, edit the file ```./urls.py``` within the function:

```
from views import (
    login,
)

def Router() -> APIRouter:
    route = APIRouter()
    route.include_router(login.router, tags=['login'])
    
    return route
```

Thanks! Every help is welcome.
