from extenstions import db


movie_genre_association = db.Table('movie_genre_association',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
    db.Column('genre_id', db.String, db.ForeignKey('genre.id'), primary_key=True)
)

class Movie(db.Model):

  __tablename__ = "movie"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200))
  imdb_score = db.Column(db.Float)
  director = db.Column(db.String(200))
  popularity = db.Column(db.Float)
  genre = db.relationship("Genre", secondary=movie_genre_association, lazy='subquery',
                          backref=db.backref('genres', lazy=True))

  @classmethod
  def get_all(cls):
    return cls.query.all()

  @classmethod
  def get_movie_by_name(cls, name):
    return cls.query.join(movie_genre_association).filter(cls.name.ilike(name)).first()

  def save(self):
    db.session.save(self)
    db.session.commit()



class Genre(db.Model):
  __tablename__ = "genre"

  id = db.Column(db.String(200), primary_key=True)

  @classmethod
  def is_exist(cls, id):
    if cls.query.filter(id).first():
      return True
    return False

