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

    # Ensure instance folder exists for deployment environments (skip on read-only filesystems)
    instance_path = app.instance_path
    try:
        if not os.path.exists(instance_path):
            os.makedirs(instance_path, exist_ok=True)
            app.logger.info(f'Created instance folder: {instance_path}')
    except OSError:
        # Read-only filesystem (e.g., Vercel, AWS Lambda)
        app.logger.warning(f'Cannot create instance folder (read-only filesystem): {instance_path}')

    # Setup logging (skip file logging on read-only filesystems)
    log_level = logging.DEBUG if app.config.get('DEBUG') else logging.INFO
    
    # Try to setup file logging
    try:
        if not os.path.exists('logs'):
            os.makedirs('logs', exist_ok=True)
        file_handler = RotatingFileHandler(
            'logs/Trydo.log', 
            maxBytes=1024*1024*10,  # 10MB
            backupCount=20
        )
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        app.logger.addHandler(file_handler)
    except (OSError, PermissionError):
        # Read-only filesystem - use console logging only
        app.logger.warning('File logging disabled (read-only filesystem)')
    
    # Always setup console logging for serverless environments
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s'
    ))
    app.logger.addHandler(console_handler)
    app.logger.setLevel(log_level)
    app.logger.info(f'Trydo startup - Debug: {app.config.get("DEBUG", False)}')

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    
    from .models import model

    # Register blueprints
    register_routes(app)

    # Provide a default ContactForm so templates using `form` don't break
    from .forms import ContactForm
    @app.context_processor
    def inject_default_form():
        try:
            return {'form': ContactForm()}
        except Exception:
            return {}

    # Register error handlers
    register_error_handlers(app)

    return app
