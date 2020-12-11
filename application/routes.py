from application import app, db   
from application.models import Tasks

@app.route("/")
@app.route("/home")
def home():
    all_tasks = Tasks.query.all() #this will return a list of all tasks
    return str(all_tasks)

@app.route("/create")
def create():
    new_todo = Task(description = "New task")
    db.session.add(new_todo)
    db.session.commit()
    return "New task added"

@app.route("/complete/<int:id>")
def complete(id):
    task = Tasks.query.filter_by(id=id).first() #we want the first one and query is to find from general tasks    
    task.completed = True
    db.session.commit()
    return f"Task {id} is now complete"

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task = Tasks.query.filter_by(id=id).first() #we want the first one and query is to find from general tasks    
    task.completed = False
    db.session.commit()
    return f"Task {id} is now incomplete"

@app.roite("/update/<new_description>")
def update(new_description):
    task = Tasks.query.order_by(Tasks.id.desc()).first() #query and order by last id we used and we use first as we want to treat it as one object and not a list
    task.description = new_description
    db.session.commit()
    return f"Most recent task was updated with the description: {new_description}"

@app.route("/delete/<int:id>")
def delete(id):
    task = Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    return f"Task {id} was deleted."