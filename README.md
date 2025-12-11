# Daily Tasks & Notes Manager

## Description
Daily Tasks & Notes Manager is a simple yet fully functional web application designed to help users organize, manage, and keep track of their daily tasks and personal notes efficiently. The application allows users to add tasks, mark them as completed, and delete them when finished. It provides a clean and intuitive interface for task management and demonstrates fundamental web development concepts using **Python**, **Flask**, **SQLite**, and **HTML/CSS with Jinja2 templates**.

This project is ideal for beginners who want to learn full-stack development, database integration, and dynamic content rendering with Flask. Users can experience how backend logic interacts with a frontend interface to perform CRUD (Create, Read, Update, Delete) operations on a database.

## Features
- **Add Task:** Users can enter new tasks into an input field and save them to the database.
- **Mark Task as Done:** Completed tasks can be marked with a check button (✅), visually distinguishing them from pending tasks.
- **Delete Task:** Users can remove unnecessary or completed tasks from their list using the delete button (❌).
- **View All Tasks:** The main page displays all tasks with their current status (done or pending), allowing easy tracking.
- **Persistent Storage:** All tasks are stored in an SQLite database (`database.db`) to ensure data is saved between sessions.
- **Simple and Clean Interface:** Using HTML/CSS with Jinja2 templates, the application provides a readable, user-friendly layout.

## How It Works
- **Backend (app.py):** Runs the Flask web server and handles routing, form submissions, and database interactions.
- **Database (database.db):** Stores task information persistently. Each task record includes:
  - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
  - `title` (TEXT NOT NULL)
  - `status` (TEXT NOT NULL, e.g., "Pending" or "Completed")
  - `created_at` (TEXT, timestamp when task was added)
- **Templates (index.html, etc.):** Render dynamic pages using Jinja2, displaying tasks with real-time updates.
- **Static Files (style.css):** Contains CSS for styling the web pages and ensuring a clean, readable interface.
- **Routes:**
  - `/` → Displays all tasks along with their status.
  - `/add` → Endpoint for adding new tasks.
  - `/done/<task_id>` → Marks a specific task as completed.
  - `/delete/<task_id>` → Deletes a specific task from the database.

## Usage Instructions
1. Ensure you have **Python** and **Flask** installed.
2. Navigate to the project folder in your terminal.
3. Start the Flask server with:
   ```bash
   flask run
Open your web browser and go to the provided URL (usually http://127.0.0.1:5000/).

Add new tasks, mark tasks as done, and delete tasks as needed.

All changes are automatically saved in database.db.

Database Structure
tasks table:

id → Unique identifier for each task (INTEGER, PRIMARY KEY, AUTOINCREMENT)

title → Task description (TEXT)

status → Task status (TEXT: "Pending" or "Completed")

created_at → Timestamp of task creation (TEXT)

Possible Improvements
Categories & Priorities: Add support for categorizing tasks or assigning priority levels.

Deadlines & Reminders: Include due dates for tasks with optional reminder notifications.

Search & Filter: Allow users to search for tasks or filter by status or category.

Real-Time Updates: Use JavaScript/AJAX to update the page without refreshing.

User Accounts: Extend the app to support multiple users with separate task lists.

Improved UI: Enhance the interface with responsive design, animations, or themes.

Testing the Application
Add multiple tasks and verify they appear correctly on the homepage.

Mark tasks as done and ensure the status updates visually and in the database.

Delete tasks and check that they are removed from both the page and the database.

Restart the server to confirm that tasks are saved persistently.

Credits
Built using Python, Flask, SQLite, HTML, CSS, and Jinja2.

Inspired by introductory web development tutorials and small productivity apps.
