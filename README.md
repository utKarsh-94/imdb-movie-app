# imdb-movie-app
Imdb Movie Sample Api

Initial Setup

  ```python -m venv menv```
  
  ```menv/Scripts/activate.bat```

Installing all required packages
  
  ```(menv) > pip install -r requirements.txt```
  
  ```(menv) > flask db init```
  
  ```(menv) > flask db migrate```
  
  ```(menv) > flask db upgrade```
  
  ```(menv) > python server.py```


There are three resources available
1) User (Handle all user functionality)
2) Movie (Handle all movie functionality)
3) Token (JWT Authroization with user_id)

For Movie Resource

| GET    | http://localhost:5000/movies | List of All Movies        |

| POST   | http://localhost:5000/movies | Create New All Movies     |

| PUT    | http://localhost:5000/movies/<string:movie> | Update Movie  |

| GET    | http://localhost:5000/movies/<string:movie> | Get Movie By Name  |


For User Resource


| GET    | http://localhost:5000/users/<string:username> | User Object|

| POST   | http://localhost:5000/users/ | Create New User |


For Token Resource

| POST    | http://localhost:5000/token/ | Access Token|






