from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import func


db = SQLAlchemy()


# class Student(db.Model):
#     __tablename__ ='students'
#     __tablename__ = 'product'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     desc = db.Column(db.String(200))
#     price = db.Column(db.Float)
#     image = db.Column(db.String, nullable=True)
#     instock = db.Column(db.Boolean)
#     created = db.Column(db.DateTime(timezone=True), default=db.func.now())
#     modified = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
