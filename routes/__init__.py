# routes/__init__.py
from .catalog import catalog_bp
from .home import home_bp


def register_blueprints(app):
    app.register_blueprint(catalog_bp)
    app.register_blueprint(home_bp)
