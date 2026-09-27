# Implement a simple task manager.
class task_manager:
    def __init__(self):
        self.tasks=["reading","writing","eating"]
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("removing imposssible")
    def add_task(self,tasks):
        self.tasks.append(tasks)
    def total_available_tasks(self):
        print(self.tasks)
        
task=task_manager()
task.remove_task("reading")
task.add_task("sleeping")
task.total_available_tasks()