from flask import Flask
from extensions import db

app = Flask(__name__)

app.config['FLASK_SECRET_KEY'] = 'A1EU4GHWeUIfkOASF0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)



if __name__ == '__main__':
    app.run(debug=True)