from typing import Any


class Base:
    id: Any
    __name__: str

    def __tablename__(cls) -> str:
        return cls.__name__.lower()
