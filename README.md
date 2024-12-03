CRUD - Python & Flask 

How to use this app?
-> There are several urls you can use:

POST             ===   curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-12-01|Meeting Notes|Discuss project updates"
LIST (GET ALL)   ===   curl http://127.0.0.1:5000/api/v1/calendar/ 
GET              ===   curl http://127.0.0.1:5000/api/v1/calendar/3/
DELETE           ===   curl http://127.0.0.1:5000/api/v1/calendar/3/ -X DELETE
PUT (UPDATE)     ===   curl http://127.0.0.1:5000/api/v1/calendar/2/ -X PUT -d "2024-12-01|Meeting Notes|Discuss project updatesss"

Author: @mrosmo
