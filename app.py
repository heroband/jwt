from flask import Flask, jsonify
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

# additional claims
@jwt.additional_claims_loader
def make_additional_claims(identity):
    if identity == "egor":
        return {'is_staff': True}
    else:
        return {'is_staff': False}


# jwt error handlers
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({
        'message': 'The token has expired.', 
        'error' : "token_expired"
    }), 401
    
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'message': 'Signature verification failed.', 
        'error' : "invalid_token"
    }), 401
    
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'message': 'Request doesnt contain valid token.', 
        'error' : "authorization_header"
    }), 401


if __name__ == '__main__':
    app.run(debug=True)