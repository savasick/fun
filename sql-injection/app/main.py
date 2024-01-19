from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

DB_NAME = "test"
DB_USER = "user"
DB_PASSWORD = "secret"
DB_HOST = "db"
DB_PORT = "5432"

conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
)
cursor = conn.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template("index.html", users=users)

@app.route("/search", methods=["POST"])
def search():
    search_term = request.form.get("search")

    cursor.execute(
        "SELECT * FROM users WHERE username='" + search_term  + "'" # cool code happen
        #"SELECT * FROM users WHERE username ILIKE %s",
        #(f"%{search_term}%",),
    )
    users = cursor.fetchall()

    return render_template("index.html", users=users, search_term=search_term)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')