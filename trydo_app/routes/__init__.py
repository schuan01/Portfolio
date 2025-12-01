from .homeViews import home_bp
from .pagesViews import pages_bp
from .serviceViews import service_bp
from .blocksViews import blocks_bp

def register_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(pages_bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(blocks_bp)