from application.app import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(120))

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    author = db.Column(db.String(80), nullable=True)
    genre = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=True)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(120),nullable=True)


# Sample for One-many and Many-Many relationship
# class WorkItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.String(120))

#     created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     shared_with = db.relationship('User', secondary=shared_with, lazy='subquery', backref=db.backref('user', lazy=True))

# shared_with = db.Table('shared_with',
#     db.Column('work_item_id', db.Integer, db.ForeignKey('work_item.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )

# Using the above sample write the DB models here



# create all tables and initialize app

db.create_all()
db.init_app(app)