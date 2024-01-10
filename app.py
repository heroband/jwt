from flask import Flask

app = Flask(__name__)

app.config['FLASK_SECRET_KEY'] = 'AIEUTGHWEUIFKOASFO'



if __name__ == '__main__':
    app.run(debug=True)