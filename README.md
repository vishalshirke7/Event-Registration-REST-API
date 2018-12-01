# Event-Registration-REST-API-

### _Tech stack used_
```
- python/django/django-restframework
- SQlite 3      
```

#### Installation

##### clone or download and extract the project directory 
1. Create a virtualenv  
```
a. virtualenv env
b. cd env
```
2. Place the downloaded project inside env
```
a. cd Event-Registration-REST-API
b. pip install requirements.txt
```

### Running the APIs. There are two apps in this project (userregistration, events)


 
##### User Registration Endpoints  (http:127.0.0.1:8000/api/v1/)
```
1. Register a new user with information -  http:127.0.0.1:8000/api/v1/register/
2. Login using credentials entered during registration -  http:127.0.0.1:8000/api/v1/login/
3. Logout -  http:127.0.0.1:8000/api/v1/driver/logout/
```
#### NOTE : while signing up with new user, logout if you are already logged in

##### Events Endpoints  (http:127.0.0.1:8000/api/v1/events/)
```
1. Create a new event -  http:127.0.0.1:8000/api/v1/events/create-event/
2. Send invitations to users for event using their email ids -  http:127.0.0.1:8000/api/v1/events/invite-users/
3. View all events  -  http:127.0.0.1:8000/api/v1/events/view-all-events/
4. Register/Unregister for any event for which an invitation has been received -  http:127.0.0.1:8000/api/v1/events/register-unregister/
5.  Limit number of attendees for an event (By changing the maximum nuber of attendees)
```

