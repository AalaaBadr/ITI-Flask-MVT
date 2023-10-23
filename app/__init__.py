from flask import Flask, render_template
from app.config import project_config as App_Config
from flask_migrate import Migrate
from app.models import db
from app.products import product_blueprint
from app.categories import category_blueprint


def create_app(config_name='dev'):
    app = Flask(__name__)
    Current_App_Config = App_Config[config_name]
    app.config["SQLALCHEMY_DATABASE_URI"] = Current_App_Config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(Current_App_Config)
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/not_found.html')

    app.register_blueprint(product_blueprint)
    app.register_blueprint(category_blueprint)

    return app
