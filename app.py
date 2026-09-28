import os
from flask import Flask, jsonify, request

app = Flask(__name__, static_folder="static")

todos = []
next_id = 1


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api")
def api_info():
    return jsonify(message="Hello from Docker!")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_todo():
    global next_id
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return jsonify(error="'title' is required"), 400
    todo = {"id": next_id, "title": title, "done": False}
    next_id += 1
    todos.append(todo)
    return jsonify(todo), 201


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify(message="deleted")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
