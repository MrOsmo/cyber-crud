from typing import List
import model
import db

HEADING_LIMIT = 30
TEXT_LIMIT = 200
EVENT_LIMIT = 1

class LogicException(Exception):
    pass
  
class EventLogic:
    def __init__(self):
        self._event_db = db.EventDB()
      
    @staticmethod
    def _validate_event(event: model.Event):
        if event is None:
            raise LogicException("Event is None")
        elif event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"Title length > MAX: {TEXT_LIMIT}")
        elif event.heading is None or len(event.heading) > HEADING_LIMIT:
            raise LogicException(f"Heading > MAX: {HEADING_LIMIT}")
          
    def create(self, event: model.Event) -> str:
        self._validate_event(event)
        existing_events = self.list()
        
        for e in existing_events:
            if e.date == event.date:
                raise LogicException(f"This event already exists on {event.date}.")
        try:
            return self._event_db.create(event)
        except Exception as ex:
            raise LogicException(f"Failed CREATE operation with: {ex}")
    
    def list(self) -> List[model.Event]:
        try:
            return self._event_db.list()
        except Exception as ex:
            raise LogicException(f"Failed LIST operation with: {ex}")
    
    def get(self, _id: str) -> model.Event:
        try:
            return self._event_db.get(_id)
        except Exception as ex:
            raise LogicException(f"Failed GET operation with: {ex}")
    
    def put(self, _id: str, event: model.Event):
        self._validate_event(event)
        try:
            return self._event_db.put(_id, event)
        except Exception as ex:
            raise LogicException(f"Failed PUT operation with: {ex}")
    
    def delete(self, _id: str):
        try: 
            return self._event_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"Failed DELETE operation with: {ex}")