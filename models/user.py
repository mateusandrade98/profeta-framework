from database.base_class import Base
from typing import Optional, Any


class User(Base):
    _id: Optional[Any]
    id: str
    name: str
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
