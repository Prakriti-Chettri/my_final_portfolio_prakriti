from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Connect to PostgreSQL (Render will give DATABASE_URL)
DATABASE_URL = os.environ.get("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Form submit
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Insert into database
    query = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, message))
    conn.commit()

    return "<h2>Saved to database ✅</h2><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)