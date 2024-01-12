from flask import Flask
from extensions import db, jwt
from auth import auth_bp
from users import user_bp

app = Flask(__name__)

app.config['FLASK_SECRET_KEY'] = 'A1EU4GHWeUIfkOASF0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True
app.config['JWT_SECRET_KEY'] = 'a497715670bb1406d2120e37'

#initialize extensions
db.init_app(app)
jwt.init_app(app)

#register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')


if __name__ == '__main__':
    app.run(debug=True)