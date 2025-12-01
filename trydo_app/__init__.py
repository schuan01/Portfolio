from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler
import os
import importlib.util
from .routes import register_routes  # helper to register all blueprints

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "instance", ".env"))

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def register_error_handlers(app):
    from flask import render_template
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('pages/pageError.html', code=404, message='Page not found'), 404
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('pages/pageError.html', code=500, message='Internal server error'), 500
    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('pages/pageError.html', code=403, message='Forbidden'), 403

def create_app(config_class=None):
    app = Flask(__name__, instance_relative_config=True)

    if config_class is not None:
        app.config.from_object(config_class)
    else:
        # Load config based on environment
        config_path = os.path.join(app.instance_path, 'config.py')
        config_env = os.environ.get('FLASK_CONFIG', 'development').lower()
        config_class_name = {
            'development': 'DevelopmentConfig',
            'production': 'ProductionConfig',
            'testing': 'TestingConfig',
        }.get(config_env, 'DevelopmentConfig')

        # Try to load from instance/config.py if it exists
        if os.path.exists(config_path):
            spec = importlib.util.spec_from_file_location('instance_config', config_path)
            instance_config = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(instance_config)
            app.config.from_object(getattr(instance_config, config_class_name))
        else:
            # Fallback to environment variables for production/serverless environments
            app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-please-change')
            app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///:memory:')
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            app.config['SESSION_COOKIE_HTTPONLY'] = True
            app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
            app.config['PERMANENT_SESSION_LIFETIME'] = 3600
            
            if config_env == 'production':
                app.config['DEBUG'] = False
                app.config['SESSION_COOKIE_SECURE'] = True
            else:
                app.config['DEBUG'] = True
                app.config['SESSION_COOKIE_SECURE'] = False

    # Ensure instance folder exists for deployment environments
    instance_path = app.instance_path
    if not os.path.exists(instance_path):
        os.makedirs(instance_path, exist_ok=True)
        app.logger.info(f'Created instance folder: {instance_path}')

    # Ensure logs directory exists
    if not os.path.exists('logs'):
        os.makedirs('logs', exist_ok=True)
    log_level = logging.DEBUG if app.config.get('DEBUG') else logging.INFO
    file_handler = RotatingFileHandler(
        'logs/Trydo.log', 
        maxBytes=1024*1024*10,  # 10MB
        backupCount=20
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(log_level)
    error_handler = RotatingFileHandler(
        'logs/Trydo_errors.log',
        maxBytes=1024*1024*5,  # 5MB
        backupCount=10
    )
    error_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]\n'
        'Exception: %(exc_info)s'
    ))
    error_handler.setLevel(logging.ERROR)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(error_handler)
    app.logger.setLevel(log_level)
    app.logger.info(f'Trydo startup - Debug: {app.config.get("DEBUG", False)}')

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    
    from .models import model

    # Register blueprints
    register_routes(app)

    # Register error handlers
    register_error_handlers(app)

    return app
