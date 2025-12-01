import os
from jobaway_app import create_app
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
from flask_wtf.csrf import generate_csrf
from dotenv import load_dotenv


config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
config_name = os.environ.get('FLASK_CONFIG', 'development')
app = create_app(config_class=config_map[config_name])

@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf)

load_dotenv()

if __name__ == '__main__':
    app.run(debug=app.config.get("DEBUG", False))
