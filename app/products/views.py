from flask import render_template

from app.products import product_blueprint


# use blueprint to collect related urls
@product_blueprint.route('/', endpoint='home')
def home():
    return render_template('layouts/index.html')
