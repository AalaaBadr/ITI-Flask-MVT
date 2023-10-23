from flask import request, redirect, url_for, render_template

from app.models import Category
from app.categories import category_blueprint


@category_blueprint.route('/categories', endpoint='categories', methods=['GET'])
def categories():
    categories = Category.get_categories()
    return render_template('category/categories.html', categories=categories)


@category_blueprint.route('/category/<int:id>', endpoint='category', methods=['GET'])
def category(id):
    category = Category.get_category(id)
    return render_template('category/category.html', category=category, products=category.products)


@category_blueprint.route('/category/add', methods=['GET', 'POST'], endpoint='add_category')
def create():
    if request.method == 'POST':
        Category.save_category(request_data=request)
        return redirect(url_for('categories.categories'))

    return render_template('category/add.html')


@category_blueprint.route('/category/update/<int:id>', methods=['GET', 'POST'], endpoint='update_category')
def update(id):
    category = Category.get_category(id)
    if request.method == 'POST':
        Category.update_category(id=id, request_data=request)
        return redirect(url_for('categories.category', id=category.id))

    return render_template('category/update.html', category=category)


@category_blueprint.route('/category/delete/<int:id>', endpoint='delete_category')
def delete(id):
    category = Category.get_category(id)
    category.delete_category()
    return redirect(url_for('categories.categories'))
