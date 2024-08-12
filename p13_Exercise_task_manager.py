class Task:
	def __init__(self, description):
		self.description = description
		self.completed = False

	def mark_completed(self):
		self.completed = True


class TaskManager:
	def __init__(self):
		self.tasks = []

	def add_task(self, task):
		self.tasks.append(task)

	def get_completed_tasks(self):
		return [task for task in self.tasks if task.completed]

	def get_incomplete_tasks(self):
		return [task for task in self.tasks if not task.completed]
