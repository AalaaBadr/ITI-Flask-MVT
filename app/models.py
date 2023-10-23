from flask import url_for
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy import func


db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    image = db.Column(db.String, nullable=True)
    products = db.relationship('Product',backref='category')

    @property
    def img_url(self):
        return url_for('static', filename=f'images/{self.image}')

    @classmethod
    def get_categories(cls):
        return cls.query.all()

    @classmethod
    def get_category(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def save_category(cls, request_data):
        category = cls(**request_data.form)

        db.session.add(category)
        db.session.commit()
        return category

    @classmethod
    def update_category(cls, request_data, id):
        category = cls.query.get_or_404(id)
        category.name = request_data.form['name']
        category.image = request_data.form['image']

        db.session.commit()
        return category

    def delete_category(self):
        db.session.delete(self)
        db.session.commit()
        return True


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
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

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
                      image=request_data.form['image'],
                      price=request_data.form['price'],
                      desc=request_data.form['desc'],
                      instock=bool(request_data.form['instock']),
                      category_id=int(request_data.form['category_id']))

        db.session.add(product)
        db.session.commit()
        return product

    @classmethod
    def update_product(cls, request_data, id):
        product = cls.query.get_or_404(id)
        product.name = request_data.form['name']
        product.price = request_data.form['price']
        product.image = request_data.form['image']
        product.desc = request_data.form['desc']
        product.instock = bool(request_data.form['instock'])
        product.category_id = int(request_data.form['category_id'])

        db.session.commit()
        return product

    def delete_product(self):
        db.session.delete(self)
        db.session.commit()
        return True
