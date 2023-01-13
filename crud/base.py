from typing import Generic, TypeVar, Dict, List, Optional
from database.base_class import Base
from database.get_database import Session
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def get(self, session: Session, id: int) -> Optional[Dict]:
        return session.find(filter=dict(id=id))

    def get_multi(self, session: Session, skip: int = 0, limit: int = 100) -> List:
        return session.all(skip=skip, limit=limit)

    def create(self, session: Session, data: Dict) -> ModelType:
        return session.put(data=data)

    def update(self, session: Session, filter: Dict, update: Dict) -> ModelType:
        return session.update(filter=filter, update=update)

    def remove(self, session: Session, id: int) -> ModelType:
        return session.delete(filter=dict(id=id))
