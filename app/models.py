from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import func


db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    desc = db.Column(db.String(200))
    price = db.Column(db.Float)
    image = db.Column(db.String, nullable=True)
    instock = db.Column(db.Boolean)
    created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    modified = db.Column(db.DateTime(timezone=True), server_onupdate=db.func.now(), server_default=db.func.now())
