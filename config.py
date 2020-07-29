class Config:
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = "sqlite:///imdb-movies.db"
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  SECRET_KEY='IMDB_APP'
  JWT_ERROR_MESSAGE_KEY = 'message'

  HOST='localhost'
  PORT=5000