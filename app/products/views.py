from flask import request, redirect, url_for, render_template

from app.models import Product, Category
from app.products import product_blueprint


@product_blueprint.route('/', endpoint='home', methods=['GET'])
def home():
    return render_template('layouts/index.html')


@product_blueprint.route('/products', endpoint='products', methods=['GET'])
def products():
    products = Product.get_products()
    return render_template('product/products.html', products=products)


@product_blueprint.route('/product/<int:id>', endpoint='product', methods=['GET'])
def product(id):
    product = Product.get_product(id)
    return render_template('product/product.html', product=product)


@product_blueprint.route('/product/add', methods=['GET', 'POST'], endpoint='add')
def create():
    categories = Category.get_categories()
    if request.method == 'POST':
        Product.save_product(request_data=request)
        return redirect(url_for('products.products'))

    return render_template('product/add.html', categories=categories)


@product_blueprint.route('/product/update/<int:id>', methods=['GET', 'POST'], endpoint='update')
def update(id):
    categories = Category.get_categories()
    product = Product.get_product(id)
    if request.method == 'POST':
        Product.update_product(id=id, request_data=request)
        return redirect(url_for('products.product', id=product.id))

    return render_template('product/update.html', product=product, categories=categories)


@product_blueprint.route('/product/delete/<int:id>', endpoint='delete')
def delete(id):
    product = Product.get_product(id)
    product.delete_product()
    return redirect(url_for('products.products'))
