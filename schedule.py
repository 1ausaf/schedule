import schedule
import time
from plyer import notification

class ScheduleApp:
    def __init__(self):
        self.schedule = {}

    def add_task(self, task_name, task_time):
        self.schedule[task_name] = task_time

    def delete_task(self, task_name):
        if task_name in self.schedule:
            del self.schedule[task_name]
            return True
        else:
            return False

    def display_schedule(self):
        if self.schedule:
            print("Your Schedule:")
            for task, time in self.schedule.items():
                print(f"{task}: {time}")
        else:
            print("Your schedule is empty.")

    def set_alarm(self, task_name):
        if task_name in self.schedule:
            task_time = self.schedule[task_name]
            schedule.every().day.at(task_time).do(self.notify, task_name)
            return True
        else:
            return False

    def notify(self, task_name):
        notification.notify(
            title="Scheduled Task",
            message=f"It's time for {task_name}!",
            timeout=10
        )

def main():
    app = ScheduleApp()

    while True:
        print("\nOptions:")
        print("1. Add task to schedule")
        print("2. Delete task from schedule")
        print("3. Display schedule")
        print("4. Set alarm for task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            task_time = input("Enter task time (HH:MM format): ")
            app.add_task(task_name, task_time)
        elif choice == "2":
            task_name = input("Enter task name to delete: ")
            if app.delete_task(task_name):
                print(f"{task_name} deleted from schedule.")
            else:
                print(f"Task '{task_name}' not found in schedule.")
        elif choice == "3":
            app.display_schedule()
        elif choice == "4":
            task_name = input("Enter task name to set alarm: ")
            if app.set_alarm(task_name):
                print(f"Alarm set for {task_name}.")
            else:
                print(f"Task '{task_name}' not found in schedule.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
