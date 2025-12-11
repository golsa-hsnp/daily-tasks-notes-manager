from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Database path
db_path = os.path.join(os.getcwd(), "database.db")

# Initialize database and tasks table
def init_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        done INTEGER DEFAULT 0,
        priority TEXT DEFAULT 'Medium',
        category TEXT DEFAULT 'General',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    priority = request.form.get("priority")
    category = request.form.get("category")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(
    "INSERT INTO tasks (description, priority, category) VALUES (?, ?, ?)",
    (task, priority, category)
)
    conn.commit()
    conn.close()
    return redirect("/")

# Mark task as done
@app.route("/done/<int:task_id>")
def done(task_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

# Delete task
@app.route("/delete/<int:task_id>")
def delete(task_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
