import os
from . import create_app
from flask_wtf.csrf import generate_csrf
from dotenv import load_dotenv

# Rely on create_app's internal env-based configuration.
app = create_app()

@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf)

load_dotenv()

if __name__ == '__main__':
    app.run(debug=app.config.get("DEBUG", False))