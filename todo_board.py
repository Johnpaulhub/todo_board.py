from flask import Flask, request, redirect, url_for

app = Flask(__name__)

TODOS = [
    {"id": 1, "task": "Review Flask deployment logs on Render", "status": "In Progress", "priority": "High"}
]

@app.route('/')
def todo_home():
    todo_html = ""
    for t in TODOS:
        color = "#f43f5e" if t['priority'] == "High" else ("#f59e0b" if t['priority'] == "Medium" else "#38bdf8")
        todo_html += f'''
        <div style="background: #1b2230; border-radius: 8px; padding: 12px; margin-bottom: 10px; border: 1px solid #2a3447; border-left: 4px solid {color}; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="font-size: 14px; font-weight: bold; color: #fff;">{t['task']}</div>
                <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">Status: <span style="color: #38bdf8;">{t['status']}</span></div>
            </div>
            <div style="font-size: 11px; background: {color}; color: #fff; padding: 3px 8px; border-radius: 4px; font-weight: bold;">{t['priority']}</div>
        </div>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart To-Do Board</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: sans-serif; background: #121824; color: #fff; margin: 0; padding: 12px; }}
            h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 6px; }}
            .card {{ background: #1b2230; padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #2a3447; }}
            input, select {{ width: 100%; padding: 10px; margin: 6px 0 12px 0; background: #121824; border: 1px solid #334155; color: #fff; border-radius: 6px; box-sizing: border-box; }}
            button {{ width: 100%; padding: 12px; background: #0284c7; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        <h2>Smart To-Do Board</h2>
        <div class="card">
            <h3 style="margin-top:0; color:#38bdf8; font-size:15px;">Add New Task</h3>
            <form action="/add_todo" method="POST">
                <input type="text" name="task" placeholder="Task description..." required>
                <select name="status">
                    <option value="To Do">To Do</option>
                    <option value="In Progress">In Progress</option>
                    <option value="Completed">Completed</option>
                </select>
                <select name="priority">
                    <option value="High">High Priority</option>
                    <option value="Medium">Medium Priority</option>
                    <option value="Low">Low Priority</option>
                </select>
                <button type="submit">+ Add Task</button>
            </form>
        </div>
        <h3 style="color: #38bdf8; margin-top: 20px;">Task Board</h3>
        {todo_html}
    </body>
    </html>
    '''

@app.route('/add_todo', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    status = request.form.get('status')
    priority = request.form.get('priority')
    if task:
        TODOS.insert(0, {"id": len(TODOS) + 1, "task": task, "status": status, "priority": priority})
    return redirect(url_for('todo_home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
