from flask import Blueprint, request, jsonify
from .db import get_cursor

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    conn, cursor = get_cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return jsonify(tasks)

@task_routes.route('/task', methods=['POST'])
def add_task():
    conn, cursor = get_cursor()
    data = request.get_json()
    cursor.execute(
        "INSERT INTO tasks (user_id, title, description, due_date) VALUES (%s, %s, %s, %s)",
        (data['user_id'], data['title'], data['description'], data['due_date'])
    )
    conn.commit()
    return jsonify({'status': 'Task Added'}), 201

@task_routes.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    conn, cursor = get_cursor()
    data = request.get_json()
    cursor.execute(
        "UPDATE tasks SET title=%s, description=%s, due_date=%s, status=%s WHERE id=%s",
        (data['title'], data['description'], data['due_date'], data['status'], task_id)
    )
    conn.commit()
    return jsonify({'status': 'Task Updated'})

@task_routes.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn, cursor = get_cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    return jsonify({'status': 'Task Deleted'})
