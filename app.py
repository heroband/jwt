from flask import Flask
from extensions import db
from auth import auth_bp

app = Flask(__name__)

app.config['FLASK_SECRET_KEY'] = 'A1EU4GHWeUIfkOASF0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True

#initialize extensions
db.init_app(app)

#register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')


if __name__ == '__main__':
    app.run(debug=True)