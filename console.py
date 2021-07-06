import pdb
from models.task import Task
from models.user import User

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository

task_repository.delete_all()

user_repository.delete_all()

user1 = User("Jack", "Jarvis")
user_repository.save(user1)
user2 = User("Victor", "McDade")
user_repository.save(user2)

print(user_repository.select_all())
# print(user_repository.select())

task = Task("Walk Dog", user1, 60)
task_repository.save(task)

print(task_repository.select_all())

# task_repository.select_all()
# user_repository.select_all()

