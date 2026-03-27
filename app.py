from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# ------------------------------
# DATABASE CONNECTION
# ------------------------------
# Use your Render PostgreSQL database URL
DATABASE_URL = "postgresql://portfolio_15a1_user:UgleefJCIBNtUPPzDxNnjAUqT8UaVszC@dpg-d723qp8ule4c73bfjov0-a.singapore-postgres.render.com/portfolio_15a1"

# Connect to PostgreSQL
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Auto-create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    message TEXT
);
""")
conn.commit()

# ------------------------------
# ROUTES
# ------------------------------

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

    # Insert data into PostgreSQL
    query = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, message))
    conn.commit()

    return "<h2>Form submitted successfully ✅</h2><a href='/'>Go Back</a>"

# Admin page to view all submitted messages
@app.route('/messages')
def messages():
    cursor.execute("SELECT id, name, email, message FROM contacts ORDER BY id DESC")
    all_messages = cursor.fetchall()  # list of tuples
    return render_template("messages.html", messages=all_messages)

# ------------------------------
# RUN APP
# ------------------------------
if __name__ == '__main__':
    app.run(debug=True)