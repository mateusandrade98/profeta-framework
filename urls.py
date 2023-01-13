from fastapi import APIRouter

from views import (
    login
)

# edit route
def Router() -> APIRouter:
    route = APIRouter()
    route.include_router(login.router, tags=['login'])

    return route
