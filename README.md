
## Install Python Dependencies

    pip install -r requirements.txt

## Install Node & SCSS Dependencies (for styling)

    npm install

## Set Environment Variables in .env file if not available Create a .env file in the project root:

    # Flask settings
    FLASK_APP=trydo_app/app.py
    FLASK_ENV=development
    FLASK_CONFIG=development
    SECRET_KEY=your-secret-key asd
    # Database
    SQLALCHEMY_DATABASE_URI=sqlite:///Trydo.db
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # CSRF
    WTF_CSRF_ENABLED=True
    # Other settings (add as needed)
    MAIL_SERVER=smtp.example.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=your-email@example.com
    MAIL_PASSWORD=your-email-password


## Database Migrations

To manage your database schema using Flask-Migrate, use the following commands:

```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

- `flask db init`: Initialize the migrations directory (run once).
- `flask db migrate -m "Message"`: Generate a migration script after model changes.
- `flask db upgrade`: Apply migrations to the database.


## Building CSS from SCSS

To compile SCSS to CSS, run:

    npm run build:css

This will compile all SCSS files in `trydo_app/static/scss/` to CSS in `trydo_app/static/css/`.


## run project (For Deployment)
    flask run


## Production Deployment

1. **Install Gunicorn** (or another WSGI server):

    pip install gunicorn

2. **Run the app with Gunicorn:**

    gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app

   (If your wsgi.py is in the root. If it's in trydo_app/, use trydo_app.wsgi:app)

3. **(Optional) Use a reverse proxy (e.g., Nginx) in front of Gunicorn for SSL, static files, etc.**

4. **Set environment variables for production:**

    - `FLASK_CONFIG=production`
    - `SECRET_KEY=your-production-secret`
    - `DATABASE_URL=your-production-db-url`
