from flask import Flask, request, jsonify
from passlib.hash import sha256_crypt
import pymysql

app = Flask(__name__)


db = pymysql.connect(
    host=' ',  
    user=' ',
    password=' ',
    db= database name
)


@app.route('/addUser', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    encrypted_password = sha256_crypt.hash(password)

    try:
        with db.cursor() as cursor:
           
            sql = "INSERT INTO user_api (username, passwd) VALUES (%s, %s)"
            cursor.execute(sql, (username, encrypted_password))
            db.commit()
        return jsonify({"message": "Registration successful!"})
    except Exception as e:
        return jsonify({"message": "An error occurred while saving the user"}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    try:
        with db.cursor() as cursor:
            
            sql = "SELECT passwd FROM user_api WHERE username = %s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()

            if result is not None:
                encrypted_password = result[0]
                
                if sha256_crypt.verify(password, encrypted_password):
                    return jsonify({"message": "Successfully logged in!"})
            return jsonify({"message": "Invalid credentials!"}), 401
    except Exception as e:
        return jsonify({"message": "An error occurred while retrieving the user"}), 500


if __name__ == '__main__':
    app.run(host= IP , port=5000)
