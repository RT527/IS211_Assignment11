# Rafi Talukder Assignment_11
from flask import Flask, render_template, request, redirect
import os
import pickle
"""---------------------------------------------------------------------------------"""
app = Flask(__name__)
"""---------------------------------------------------------------------------------"""
TODO_FILE = "todo_list.pkl"
if os.path.exists(TODO_FILE):
    with open(TODO_FILE, "rb") as f:
        todo_list = pickle.load(f)
else:
    todo_list = []
"""---------------------------------------------------------------------------------"""
@app.route('/') # Homepage
def index():
    return render_template("index.html", items=todo_list)
"""---------------------------------------------------------------------------------"""
@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get("task", "").strip()
    email = request.form.get("email", "").strip()
    priority = request.form.get("priority", "").strip()
    # Basic email validation
    if "@" not in email or "." not in email:
        return redirect('/')
    # Priority validation
    if priority not in ["Low", "Medium", "High"]:
        return redirect('/')
    # Task cannot be empty
    if task == "":
        return redirect('/')
    # Append new item
    todo_list.append({
        "task": task,
        "email": email,
        "priority": priority
    })
    return redirect('/')
"""---------------------------------------------------------------------------------"""
@app.route('/clear', methods=['POST']) # Clears post
def clear():
    todo_list.clear()
    return redirect('/')
"""---------------------------------------------------------------------------------"""
# This is the extra credit to save file
@app.route('/save', methods=['POST'])
def save():
    with open(TODO_FILE, "wb") as f:
        pickle.dump(todo_list, f)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
