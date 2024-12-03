from typing import List
import model
import storage

class DBException(Exception):
    pass
  
class EventDB:
    def __init__(self):
        self._storage = storage.LocalStorage()
        
    def create(self, event: model.Event) -> str:
        try:
            return self._storage.create(event)
        except Exception as ex:
            raise DBException(f"Failed CREATE operation with: {ex}")
    
    def list(self) -> List[model.Event]:
        try:
            return self._storage.list()
        except Exception as ex:
            raise DBException(f"Failed LIST operation with: {ex}")
    
    def get(self, _id: str) -> model.Event:
        try:
            return self._storage.get(_id)
        except Exception as ex:
            raise DBException(f"Failed GET operation with: {ex}")
    
    def put(self, _id: str, event: model.Event):
        try:
            return self._storage.put(_id, event)
        except Exception as ex:
            raise DBException(f"Failed PUT operation with: {ex}")
    
    def delete(self, _id: str):
        try:
            return self._storage.delete(_id)
        except Exception as ex:
            raise DBException(f"Failed DELETE operation with: {ex}")