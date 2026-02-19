class Facilitator:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the facilitator's task list."""
        self.tasks.append(task)

    def run_all(self):
        """Run all tasks in the order they were added."""
        results = []
        for task in self.tasks:
            result = task()
            results.append(result)
        return results

# Example usage:
if __name__ == "__main__":
    facilitator = Facilitator()

    # Define some example tasks
    def task1():
        print("Running task 1")
        return "Task 1 complete"

    def task2():
        print("Running task 2")
        return "Task 2 complete"

    facilitator.add_task(task1)
    facilitator.add_task(task2)

    results = facilitator.run_all()
    print("Results:", results)
