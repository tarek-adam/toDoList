class Task_Manager:
    def __init__(self):
        self.tasks = []  # Initialize the list of tasks

    def add(self):
        add_task = input("Enter the task to add: ").strip()  # Ask the user for the task to add
        self.tasks.append(add_task)  # Add the task to the list
        print("Task added successfully.")

    def show(self):
        if self.tasks:  # Check if the list of tasks is not empty
            print("Tasks to be done:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks to be done at the moment.")

    def delete(self):
        if self.tasks:  # Check if the list of tasks is not empty
            delete_task = input("Enter the task to be deleted: ").strip()
            if delete_task in self.tasks:  # Check if the task exists in the list
                self.tasks.remove(delete_task)  # Remove the task from the list
                print("Task deleted successfully.")
            else:
                print("Task not found.")
        else:
            print("The list of tasks is empty.")

    def start_user_interface(self):
        while True:
            print("\n1. Add a task")
            print("2. Delete a task")
            print("3. Show tasks")
            print("4. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add()
            elif choice == "2":
                self.delete()
            elif choice == "3":
                self.show()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

# Example of using the Task_Manager class
if __name__ == "__main__":
    manager = Task_Manager()
    manager.start_user_interface()
