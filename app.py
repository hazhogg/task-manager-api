from flask import Flask, request, jsonify
from models import db, Task


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
db.init_app(app)


with app.app_context():
    db.create_all()

#Get all Tasks

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks])


#Get one task

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict())


#POST - create a task

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400
    
    task = Task(
        title=data["title"],
        description=data.get("description", "")
    )

    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

#PUT - update a task
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query_or_404(id)
    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.done = data.get("done", task.done)

    db.session.commit()
    return jsonify(task.to_dict())


#DELETE - delete task

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})


#Start the app
if __name__ == "__main__":
    app.run(debug=True)
