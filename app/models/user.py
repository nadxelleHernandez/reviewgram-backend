from app import db

class User(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      name = db.Column(db.String(100), nullable=False)
      email = db.Column(db.String(100),nullable=False )
      user_name = db.Column(db.String(50), nullable=False)
      password = db.Column(db.String(50), nullable=False)
      watchlist = db.relationship("Watchlist", back_populates="user")
      reviews = db.relationship("Reviews", back_populates="user")

