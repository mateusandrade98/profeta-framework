from core.security import get_password_hash, verify_password
from typing import Dict, Optional
from database.get_database import Session
from crud.base import CRUDBase
from models.user import User
from schemas.user import UserBase, UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, session: Session, email: str) -> Optional[User | Dict]:
        return session.find(filter=dict(email=email))

    def create(self, session: Session, user: UserBase) -> User:
        return session.put(data=user.dict())

    def update(self, session: Session, id: str, update: UserBase) -> Optional[Dict]:
        update = update.dict()
        if update["password"]:
            hashed_password = get_password_hash(update["password"])
            del update["password"]
            update["hashed_password"] = hashed_password
        return session.update(filter=dict(id=id), update=update)

    def authenticate(self, session: Session, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(session=session, email=email)
        if not user:
            return None
        if not verify_password(plain_password=password, hashed_password=user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser()
