from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task list
task_list = []

# Route to view tasks
@app.route('/tasks', methods=['GET'])
def view_tasks():
    return jsonify(task_list), 200

# Route to add a task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    if task:
        task_list.append(task)
        return jsonify({"message": "Task added successfully"}), 201
    return jsonify({"error": "No task provided"}), 400

# Route to delete a task by index
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(task_list):
        deleted_task = task_list.pop(task_id)
        return jsonify({"message": f"Task '{deleted_task}' deleted successfully"}), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
