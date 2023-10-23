from flask import url_for
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
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_onupdate=db.func.now(), server_default=db.func.now())

    @property
    def img_url(self):
        return url_for('static', filename=f'images/{self.image}')

    @classmethod
    def get_products(cls):
        return cls.query.all()

    @classmethod
    def get_product(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def save_product(cls, request_data):
        product = cls(name=request_data.form['name'],
                      image=request_data.form['file'],
                      price=request_data.form['price'],
                      desc=request_data.form['desc'],
                      instock=bool(request_data.form['instock']))

        db.session.add(product)
        db.session.commit()
        return product

    @classmethod
    def update_product(cls, request_data, id):
        product = cls.query.get_or_404(id)
        product.name = request_data.form['name']
        product.price = request_data.form['price']
        product.image = request_data.form['file']
        product.desc = request_data.form['desc']
        product.instock = bool(request_data.form['instock'])

        db.session.commit()
        return product

    def delete_product(self):
        db.session.delete(self)
        db.session.commit()
        return True
