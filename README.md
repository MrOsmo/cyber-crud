CRUD - Python & Flask 

-> This app is a CRUD-based API for managing calendar events. You can:

- Create new events with a date, heading and description.
- List all events.
- Read details of a specific event by its ID.
- Update an event’s details.
- Delete an event by its ID.

========================================================================

To use this project you have to:

- Create a virtual environment (with virtualenv)
- Activate this virtual environment (in Powershell for example)
- Download packages
- Switch to acme folder (cd acme/)
- Start the project (python api.py)
  
========================================================================

How to use this app?
-> There are several methods you can use:

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

*** POST METHOD ***

curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-12-01|Meeting|Team meeting. We have to discuss our future planss."

-------------------------
*** LIST METHOD (GET ALL METHOD) ***

curl http://127.0.0.1:5000/api/v1/calendar/ 

-------------------------
*** GET METHOD ***

curl http://127.0.0.1:5000/api/v1/calendar/3/

-------------------------
*** DELETE METHOD ***

curl http://127.0.0.1:5000/api/v1/calendar/3/ -X DELETE

-------------------------
*** PUT METHOD ***

curl http://127.0.0.1:5000/api/v1/calendar/2/ -X PUT -d "2024-12-1|Birthday Party|Celebrating."

Author: @mrosmo
