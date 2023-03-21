from models.task import Task
from models.user import User
import repositories.task_repository as task_repository
import repositories.user_repository as user_repository

task_repository.delete_all()
user_repository.delete_all()

# we created user1 and user2 for user.py;
# we created task1 and task2 for task.py
# we assign task1 to user1 & task2 to user2 in this console.py so that  
# we can directly get user_id by simply using task.user.id in task_repository

user1 = User("Jack", "Jarvis")
user_repository.save(user1)

user2 = User("Victor", "MaDade")
user_repository.save(user2)

task1 = Task("Pick up milk", user1, 30)
task_repository.save(task1)

task2 = Task("Hoovering", user2, 40)
task_repository.save(task2)

task1.description = "Pick up Oat milk"
task_repository.update(task1)

result = task_repository.select_all()

for task in result:
    print(f"{task.description} is assigned to {task.user.first_name}")

user1_tasks = task_repository.tasks_for_user(user1)
for task in user1_tasks:
    print(f"{task.description}")

