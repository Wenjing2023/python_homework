from db.run_sql import run_sql
from models.task import Task
import repositories.user_repository as user_repository

def select_all():
    tasks = []
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row["user_id"])
        # select() is the function from user_repository.py
        # create a new task object 
        new_task = Task(row["description"], user, row["duration"], row["completed"], row["id"])
        # append to the list
        tasks.append(new_task)
    return tasks

# delete_all
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)
# delete(id)
def delete(id):
    sql = "DELETE FROM tasks WHERE id =%s"
    values = [id]
    run_sql(sql, values)
# values is a list cause run_sql is expecting it to be a list


# create(task)
def save(task):
    sql = "INSERT INTO tasks(description, user_id, duration, completed) VALUES (%s,%s,%s,%s) RETURNING *"
    # %s only used in psycopg2; run_sql is using psycopg2
    values = [task.description, task.user.id, task.duration, task.completed]
    # task.user.id is from user.py??
    results = run_sql(sql, values)
    # result is a list of one dic, looks like this [{'id':3, 'description': 'Pick up milk', ... }]
    # each row is dic 
    id = results[0]['id']
    task.id = id
    return task

# slect(id)
def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    # %s is a variable, is the id in values = [id]
    values = [id]
    results = run_sql(sql, values)
    if len(results) > 0:
        selected_task = results[0]
        user = user_repository.select(selected_task["user_id"])
        task = Task(
            selected_task["description"],
            user,
            selected_task["duration"],
            selected_task["completed"],
            selected_task["id"]
        )
    return task

# update(task)
def update(task):
    sql = """UPDATE tasks 
            SET (description, user_id, duration, completed) = (%s,%s,%s,%s) 
            WHERE id = %s"""
    values = [task.description, task.user.id, task.duration, task.completed, 
              task.id]
    # values has to be in the right order
    run_sql(sql, values)

def tasks_for_user(user):
    sql = "SELECT * FROM tasks WHERE user_id =%s"
    values = [user.id]
    results = run_sql(sql, values)
    user_tasks = []
    for row in results:
        task = Task(row["description"], user, row["duration"], row["completed"], row["id"])
        user_tasks.append(task)
    return user_tasks
