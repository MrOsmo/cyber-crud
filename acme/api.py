from flask import Flask
from flask import request
import model
import logic
import json

app = Flask(__name__)

_event_logic = logic.EventLogic()

class ApiException(Exception):
    pass
  
API_ROOT = "/api/v1"
EVENT_API_ROOT = API_ROOT + "/calendar"

def _from_raw(raw_event: str) -> model.Event:
    parts = raw_event.split('|')
    if len(parts) != 3:
        raise ApiException("Invalid format. Expected 'YYYY-MM-DD|heading|description'.")

    event = model.Event()
    event.date = parts[0]
    event.heading = parts[1]
    event.text = parts[2]
    return event


def _to_raw(event: model.Event) -> str:
    if event.id is None:
        return f"{event.date}|{event.heading}|{event.text}"
    else:
        return f"{event.id}|{event.date}|{event.heading}|{event.text}"

@app.route(EVENT_API_ROOT + "/", methods=["POST"])
def create():
   try:
       data = request.get_data().decode('utf-8')
       event = _from_raw(data)
       _id = _event_logic.create(event)
       return f"new id: {_id}", 201

   except Exception as ex:
        raise ApiException(f"Failed to CREATE with: {ex}", 404)

@app.route(EVENT_API_ROOT + "/", methods=["GET"]) 
def list():
     try:
         events = _event_logic.list()
         raw_events = ""
         for note in events:
             raw_events += _to_raw(note) + '\n'
         return raw_events, 200
     except Exception as ex:
        return ApiException(f"Failed to LIST with: {ex}", 404)


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["GET"])
def get(_id: str):
    try:
        event = _event_logic.get(_id)
        raw_event = _to_raw(event)
        return raw_event, 200
    except Exception as ex:
        return  ApiException(f"Failed to READ with: {ex}", 404)


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["PUT"])
def put(_id: str):
    try:
        data = request.get_data().decode('utf-8')
        event = _from_raw(data)
        _event_logic.put(_id, event)
        return "Updated", 200
    except Exception as ex:
        return f"Failed to UPDATE with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _event_logic.delete(_id)
        return "Deleted", 200
    except Exception as ex:
        return ApiException(f"Failed to DELETE with: {ex}", 404)
      
      
      
if __name__ == "__main__":
    app.run(debug=True)