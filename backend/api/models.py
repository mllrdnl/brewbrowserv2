# from flask_sqlalchemy import SQLAlchemy
# from app import app
# from flask_marshmallow import Marshmallow


# db = SQLAlchemy(app)
# ma = Marshmallow(app)

# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.email

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }


# class Beer(db.Model):
#     __tablename__ = 'beer'
#     id = db.Column(db.String(100), primary_key=True)
#     name = db.Column(db.String(200), unique=False, nullable=False)

#     def __repr__(self):
#         return '<Beer %r>' % self.id

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.email
#         }
    

# class BeerDetails(db.Model):
#     __tablename__ = 'beerdetails'
#     id = db.Column(db.String(100), primary_key=True)
#     obj = db.Column(db.JSON, unique=False, nullable=False)
#     name = db.Column(db.String(200), unique=False, nullable=False)
#     style = db.Column(db.String(120), unique=False, nullable=False)
#     description = db.Column(db.String(300), unique=False, nullable=True)
#     abv = db.Column(db.Float, unique=False, nullable=True)
#     ibu = db.Column(db.Integer, unique=False, nullable=True)
#     cb_verified = db.Column(db.Boolean, unique=False, nullable=True)
#     brewer_verified = db.Column(db.Boolean, unique=False, nullable=True)
#     brewer = db.Column(db.String(80), unique=False, nullable=True)

#     def __repr__(self):
#         return '<beerdetails %r>' % self.id

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "style": self.style,
#             "description": self.description,
#             "abv": self.abv,
#             "ibu": self.ibu,
#             "brewer": self.brewer
#         }


# class BeerSchema(ma.ModelSchema):
#     class Meta:
#         model = Beer
#         sqla_session = db.session