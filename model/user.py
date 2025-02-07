import mysql.connector as mysql
from app import bcrypt
from model.model import Model
from flask import make_response as response
import jwt

class User(Model):
    def __init__(self):
        """
        Initialize a connection to the database and set
        self.cursor to a MySQLCursor object.
        """
        self.db = mysql.connect(
            host="localhost",
            user="root",
            passwd="",
            database="dumiapiflask"
        )
        self.db.autocommit = True
        self.cursor = self.db.cursor()
        if self.cursor:
            print("Connected to MySQL")
            pass
        else:
            return response(jsonify({'status':False,'error': 'Failed to connect to MySQL'}), 500)

    def login(self, data):
        self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (data['username']))
        user = self.cursor.fetchone()
        if user:
            if bcrypt.check_password_hash(user['password'], data['password']):
                user.pop('password')
                return response(jsonify({'status':True, 'message': 'Login successful', 'data': jwt.encode(payload=user, key=self.secret_key, algorithm='HS256')}), 200)
        else:
            return response(jsonify({'status':False,'error': 'Invalid username or password'}), 401)

