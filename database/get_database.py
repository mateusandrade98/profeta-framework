from core.config import settings
from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Dict, List, AnyStr


class Session:
    def __init__(self, session: Collection = None):
        self.session = session
        if self.session is None:
            self.session = self.get_connection()

    def get_connection(self, collections: AnyStr = None):
        client = MongoClient(settings.MONGO_CONNECTION_STRING)
        if not collections:
            self.session = client[settings.MONGO_DATABASE].get_collection(settings.MONGO_COLLECTIONS)
            return self.session
        self.session = client[settings.MONGO_DATABASE].get_collection(collections)
        return self.session

    def all(self, skip: int = 0, limit: int = 100) -> List:
        cursor = self.session.find().skip(skip).limit(limit)
        data = []
        for item in cursor:
            data.append(item)
        return data

    def find(self, filter: Dict) -> Dict:
        return self.session.find_one(filter=filter)

    def put(self, data: Dict):
        return self.session.insert_one(data)

    def update(self, filter: Dict, update: Dict):
        return self.session.update_one(filter=filter, update={"$set": update})

    def delete(self, filter: Dict):
        return self.session.delete_one(filter=filter)
