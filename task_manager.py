# ===== Importing external modules ===========
'''This is the section where you will import modules'''
import os
import datetime
import sys

# Function to register a new user
def reg_user(users, current_username):
    """
    Registers a new user if the current user is 'admin'.
    Prompts for new username and password, checks for duplicates,
    and writes the new user to user.txt if valid.
    """
    
    if current_username != 'admin':
        print("You do not have permission to register a new user.")
        return

    # Prompt for new username and password
    new_username = input("Enter new username: ").lower()
    new_password = input("Enter new password: ").lower()
    confirm_password = input("Confirm new password: ").lower()

    # Check if username already exists
    with open("user.txt", "r") as file:
        for line in file:
            if new_username in line:
                print("Username already exists. Please choose a different username.")
                return

    # If passwords match, add new user
    if new_password == confirm_password:
        with open("user.txt", "a") as file:
            file.write(f"{new_username}, {new_password}\n")
        print("User registered successfully")
    else:
        print("Passwords do not match. Please try again.")

# --------------------------------------------------

# Function to add a new task
def add_task():
    """
    Adds a new task to task.txt.
    Prompts for username, title, description, and due date.
    Stores the task with the current date and marks it as not completed.
    """

    # Prompt for task details
    username = input("Enter the username of the person assigned to the task: ").lower()
    title = input("Enter the title of the task: ").lower()
    description = input("Enter the description of the task: ").lower()
    due_date = input("Enter the due date of the task: ").lower()
    current_date = input("Enter the current date: ").lower()

    # Write the new task to the file
    with open("tasks.txt", "a") as file:
        file.write(f"{username}, {title}, {description}, {due_date}, {current_date}, No\n")
    print("Task added successfully!")

# Function to view all tasks
def view_all():
    """
    Displays all tasks from task.txt in a readable format.
    """

    # Read and display each task
    with open("tasks.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) < 6:
                continue
            print(f"Username: {parts[0]}")
            print(f"Title: {parts[1]}")
            print(f"Description: {parts[2]}")
            print(f"Due Date: {parts[3]}")
            print(f"Current Date: {parts[4]}")
            print(f"Completed: {parts[5]}")
            print("-" * 20)

# Function to view tasks assigned to the current user
def view_mine(current_username):
    """
    Displays all tasks assigned to the current user.
    If no tasks are found, notifies the user.
    """

    user_tasks = []
    # Read tasks and collect those assigned to the current user
    with open("tasks.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if parts[0] == current_username:
                user_tasks.append(parts)
                print(f"Task {len(user_tasks)}:")
                print(f"  Username: {parts[0]}")
                print(f"  Title: {parts[1]}")
                print(f"  Description: {parts[2]}")
                print(f"  Due Date: {parts[3]}")
                print(f"  Current Date: {parts[4]}")
                print(f"  Completed: {parts[5]}")
                print("-" * 20)
    if not user_tasks:
        print("No tasks found for this user.")
        return

    # Ask for task number to view or edit specific task
    try:
        task_number = int(input(f"Enter the task number to view/edit (1-{len(user_tasks)}), or 0 to cancel: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if task_number < 1 or task_number > len(user_tasks):
        print("Invalid task number. Please try again.")
        return

    parts = user_tasks[task_number - 1]

    print(f"Selected Task {task_number}:")
    print(f"  Username: {parts[0]}")
    print(f"  Title: {parts[1]}")
    print(f"  Description: {parts[2]}")
    print(f"  Due Date: {parts[3]}")
    print(f"  Current Date: {parts[4]}")
    print(f"  Completed: {parts[5]}")

    # Prevent editing if the task is completed
    if parts[5].lower() == "yes":
        print("This task is marked as completed and cannot be edited.")
        return

    # Edit options
    print("What would you like to edit?")
    print("1. Username")
    print("2. Title")
    print("3. Description")
    print("4. Due Date")
    print("5. Current Date")
    print("6. Completed Status")
    print("-1. return to menu")
    try:
        edit_choice = int(input("Enter the number of the field to edit: "))
    except ValueError:
        print("Invalid input.")
        return

    if edit_choice == -1:
        print("Returning to menu.")
        return

    # Read all tasks for updating
    with open("tasks.txt", "r") as file:
        all_lines = [l.strip().split(", ") for l in file.readlines()]

    idx = 0
    for i, task in enumerate(all_lines):
        if task[0] == current_username:
            idx += 1
            if idx == task_number:
                if edit_choice == 1:
                    new_username = input("Enter the new username: ").lower()
                    task[0] = new_username
                elif edit_choice == 2:
                    new_title = input("Enter the new title: ").lower()
                    task[1] = new_title
                elif edit_choice == 3:
                    new_desc = input("Enter the new description: ").lower()
                    task[2] = new_desc
                elif edit_choice == 4:
                    new_due = input("Enter the new due date (YYYY-MM-DD): ")
                    task[3] = new_due
                elif edit_choice == 5:
                    new_date = input("Enter the new current date (YYYY-MM-DD): ")
                    task[4] = new_date
                elif edit_choice == 6:
                    new_completed = input("Is the task completed? (yes/no): ").lower()
                    task[5] = new_completed
                else:
                    print("Invalid field number.")
                all_lines[i] = task
                break

    # Write updated tasks back to file
    with open("tasks.txt", "w") as file:
        for task in all_lines:
            file.write(", ".join(task) + "\n")
    print("Task updated successfully.")

# Function to view completed tasks
def view_completed():
    """
    Displays all tasks that are marked as completed in task.txt.
    """

    # Read and display only completed tasks
    with open("tasks.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) < 6:
                continue
            if parts[5].lower() == "yes":
                print(f"Username: {parts[0]}")
                print(f"Title: {parts[1]}")
                print(f"Description: {parts[2]}")
                print(f"Due Date: {parts[3]}")
                print(f"Current Date: {parts[4]}")
                print(f"Completed: {parts[5]}")
                print("-" * 20)

# Function to delete all tasks marked as not completed
def delete_task():
    """
    Deletes a specific task selected by the user from task.txt.
    Shows all tasks with numbers, prompts for the number to delete,
    and removes only that task from the file.
    """

    # Read all tasks
    with open("tasks.txt", "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines:
        print("No tasks to delete.")
        return

    # Display all tasks with numbers
    print("Tasks:")
    for idx, line in enumerate(lines, 1):
        parts = line.split(", ")
        print(f"{idx}. Username: {parts[0]}, Title: {parts[1]}, Description: {parts[2]}, Due Date: {parts[3]}, Current Date: {parts[4]}, Completed: {parts[5]}")

    try:
        task_num = int(input(f"Enter the number of the task to delete (1-{len(lines)}), or 0 to cancel: "))
    except ValueError:
        print("Invalid input.")
        return

    if task_num == 0:
        print("Delete cancelled.")
        return
    if not (1 <= task_num <= len(lines)):
        print("Invalid task number.")
        return

    # Remove the selected task
    del lines[task_num - 1]

    # Write the remaining tasks back to the file
    with open("tasks.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")

    print("Task deleted successfully.")

# Function to generate a task overview report
def generate_report():
    """
    Generates a task overview report and writes it to task_overview.txt.
    Includes statistics on total, completed, uncompleted, and overdue tasks.
    """

    # Read all tasks
    with open("tasks.txt", "r") as file:
        lines = file.readlines()
    # Count total tasks
    total_tasks = len(lines)
    # Count completed, uncompleted, and overdue tasks

    completed_tasks = sum(1 for line in lines if line.strip().split(", ")[5].lower() == "yes")

    uncompleted_tasks = total_tasks - completed_tasks

    overdue_tasks = sum(
        1 for line in lines
        if line.strip().split(", ")[5].lower() == "no" and
        datetime.datetime.strptime(line.strip().split(", ")[3], "%Y-%m-%d") < datetime.datetime.now()
    )
    completed_percentage = (completed_tasks / total_tasks * 100) if total_tasks else 0
    overdue_percentage = (overdue_tasks / total_tasks * 100) if total_tasks else 0

    # Write report to file
    with open("task_overview.txt", "w") as file:
        file.write(f"Total number of tasks: {total_tasks}\n")
        file.write(f"Number of completed tasks: {completed_tasks}\n")
        file.write(f"Number of uncompleted tasks: {uncompleted_tasks}\n")
        file.write(f"Number of uncompleted tasks that are overdue: {overdue_tasks}\n")
        file.write(f"Percentage of completed tasks: {completed_percentage:.2f}%\n")
        file.write(f"Percentage of uncompleted tasks that are overdue: {overdue_percentage:.2f}%\n")

# Function to generate a user overview report
def generate_user_report(users):
    """
    Generates a user overview report and writes it to user_overview.txt.
    Includes statistics for each user: number of tasks, completion rates, and overdue tasks.
    """

    # Read all tasks
    with open("tasks.txt", "r") as file:
        lines = file.readlines()
    total_users = len(users)
    total_tasks = len(lines)

    # Write user statistics to file
    with open("user_overview.txt", "w") as file:
        file.write(f"Total number of users: {total_users}\n")
        file.write(f"Total number of tasks: {total_tasks}\n")
        for user in users:
            user_tasks = [line for line in lines if line.strip().split(", ")[0] == user]
            num_user_tasks = len(user_tasks)
            user_percentage = (num_user_tasks / total_tasks * 100) if total_tasks else 0
            completed_tasks = sum(1 for line in user_tasks if line.strip().split(", ")[5].lower() == "yes")
            completed_percentage = (completed_tasks / num_user_tasks * 100) if num_user_tasks else 0
            uncompleted_tasks = num_user_tasks - completed_tasks
            uncompleted_percentage = (uncompleted_tasks / num_user_tasks * 100) if num_user_tasks else 0
            overdue_tasks = sum(
                1 for line in user_tasks
                if line.strip().split(", ")[5].lower() == "no" and
                datetime.datetime.strptime(line.strip().split(", ")[3], "%Y-%m-%d") < datetime.datetime.now()
            )
            overdue_percentage = (overdue_tasks / num_user_tasks * 100) if num_user_tasks else 0
            file.write(f"\nUser: {user}\n")
            file.write(f"Total number of tasks assigned: {num_user_tasks}\n")
            file.write(f"Percentage of total tasks assigned: {user_percentage:.2f}%\n")
            file.write(f"Percentage completed: {completed_percentage:.2f}%\n")
            file.write(f"Percentage uncompleted: {uncompleted_percentage:.2f}%\n")
            file.write(f"Percentage overdue: {overdue_percentage:.2f}%\n")

# Function to display statistics from report files
def display_statistics():
    """
    Displays the contents of task_overview.txt and user_overview.txt.
    """

    # Display task overview
    with open("task_overview.txt", "r") as file:
        for line in file:
            print(line.strip())

    # Display user overview
    with open("user_overview.txt", "r") as file:
        for line in file:
            print(line.strip())

# Main function to run the task manager application
def main():
    """
    Main function to run the task manager application.
    Handles user login and menu navigation.
    """

    # Load users from file
    users = {}
    with open("user.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(", ")
            users[username] = password

    # User login loop
    while True:
        username = input("Enter username: ").lower()
        password = input("Enter password: ").lower()
        if username in users and users[username] == password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password.")

    # Main menu loop
    while True:
        menu = input(
            '''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete task
ds - display statistics
gr - generate report
e - exit
: '''
        ).lower()

        # Handle menu options
        if menu == "r":
            reg_user(users, username)
        elif menu == "a":
            add_task()
        elif menu == "va":
            view_all()
        elif menu == "vm":
            view_mine(username)
        elif menu == "vc":
            view_completed()
        elif menu == "del":
            delete_task()
        elif menu == "gr":
            generate_report()
            generate_user_report(users)
            print("Reports generated successfully.")
        elif menu == "ds":
            # Check if report files exist, generate if not
            if not (os.path.exists("task_overview.txt") and os.path.exists("user_overview.txt")):
                generate_report()
                generate_user_report(users)
                print("Reports generated successfully.")
            display_statistics()
        elif menu == "e":
            print("Goodbye!!!")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()