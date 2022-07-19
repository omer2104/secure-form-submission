from flask import Flask, render_template, request, flash, jsonify
from sqlalchemy import true
import sqlite3
from verifyEmail import verifyEmail
from verifyCaptcha import verifyCaptcha


app = Flask(__name__)
app.secret_key = "22923"


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("info.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submitPost():
    conn = db_connection()
    cursor = conn.cursor()
    data = request.json
    review_data = data['review']
    user_data = data['user']
    recaptchaToken = data['recaptchaToken']

    isNoRobot = verifyCaptcha(recaptchaToken)

    if not isNoRobot: # If the user did not pass the recaptcha test
        return jsonify({
            "status": "Recaptcha Test Failed"
        })
    
    productName, days, satisfaction, verdict = review_data.values()
    name, email, credential = user_data.values()
    
    
    isEmailVerified = verifyEmail(credential)

    if not isEmailVerified:
        return jsonify({
            "status": "Invalid Sign In with Gmail"
        })

    sql = """INSERT INTO reviews (name, email, productName, days, satisfaction, verdict)
                        VALUES (?, ?, ?, ?, ?, ?)"""
    cursor = cursor.execute(sql, (name, email, productName, days, satisfaction, verdict))
    conn.commit()

    return jsonify({
        "status": "Saved Review!"
    })


@app.route('/dataBase.html', methods=['POST', 'GET'])
def dataBase():
    if request.method == "GET":
        conn = db_connection()
        cursor = conn.cursor()
        cursor = conn.execute("SELECT * FROM reviews")
        items = cursor.fetchall()
        return render_template('dataBase.html', items=items)
    else:
        return render_template("dataBase.html")


if __name__ == "__main__":
    app.run(debug=true, port=5500)



# @app.route('/', methods=['POST'])
# def home():
#     conn = db_connection()
#     cursor = conn.cursor()

#     if request.method == 'POST':
#         emailToAdd = request.form['email']
#         contentToAdd = request.form['content']
#         sql = """INSERT INTO info (email, content)
#                         VALUES (?, ?)"""
#         cursor = cursor.execute(sql, (emailToAdd, contentToAdd))
#         conn.commit()
#         flash("your message has been sent successfully", "info")
#         return render_template("requests.html", content="sffg")
#     else:
#         return render_template("requests.html", content="sffg")