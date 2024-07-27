from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dfhtdfg dfgherth'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # registered the previously defined blueprint
    # told my main Flask application to use the
    # blueprint and include its routes

    return app