from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os
auth = HTTPBasicAuth()
USER = "admin"
PASS = os.getenv("SECRET_PASS", "admin")
pw_hash = generate_password_hash(PASS)
@auth.verify_password
def verify(user, pwd):
    return user == USER and check_password_hash(pw_hash, pwd)