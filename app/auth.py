import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

SECRET_KEY = 'your_secret_key'  # Change this to your secret key
TOKEN_EXPIRY = 24  # Token expiry time in hours

# Function to generate JWT token

def create_token(user_id):
    expiry = datetime.utcnow() + timedelta(hours=TOKEN_EXPIRY)
    token = jwt.encode({'user_id': user_id, 'exp': expiry}, SECRET_KEY, algorithm='HS256')
    return token

# Function to validate JWT token

def validate_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Function to hash passwords

def hash_password(password):
    return generate_password_hash(password)

# Function to check password

def check_user_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)
