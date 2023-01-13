from database import get_database
from models.user import User
from core.config import settings
from core.security import get_id
from schemas.user import UserCreate
import crud

SessionLocal = get_database.Session()


def user() -> User:
    user = crud.user.get_by_email(session=SessionLocal, email=settings.FIRST_SUPERUSER_EMAIL)

    if not user:
        user_in = UserCreate(
            id=get_id(),
            name=settings.FIRST_SUPERUSER_NAME,
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )

        crud.user.create(session=SessionLocal, user=user_in)
        return crud.user.get_by_email(session=SessionLocal, email=settings.FIRST_SUPERUSER_EMAIL)

    return user
