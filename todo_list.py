# todo_list.py 
class TodoList: 
    def __init__(self): 
    # Initialise an empty list to store tasks 
        self.tasks = [] 
    def add_task(self, task): 
    # Add a new task to the list 
        self.tasks.append(task) 
    def update_task(self, old_task, new_task): 
        # Update an existing task in the list 
        if old_task in self.tasks: 
            index = self.tasks.index(old_task) 
            self.tasks[index] = new_task 
    def remove_task(self, task): 
        # Remove a task from the list 
        if task in self.tasks: 
            self.tasks.remove(task) 

# test_todo_list.py 
import unittest 
from todo_list import TodoList 
 
class TestTodoList(unittest.TestCase): 
    def setUp(self): 
        # Create a new TodoList instance before each test 
        self.todo_list = TodoList() 
 
    def test_add_task(self): 
        # Test if add_task method correctly adds a task 
        self.todo_list.add_task("Task 1") 
        self.assertEqual(self.todo_list.tasks, []) 
 
    def test_update_task(self): 
        # Test if update_task method correctly updates an existing task 
        self.todo_list.add_task("Task 1") 
        self.todo_list.update_task("Task 1", "Updated Task 1") 
        self.assertEqual(self.todo_list.tasks, ["Updated Task 1"]) 
 
    def test_remove_task(self): 
        # Test if remove_task method correctly removes a task 
        self.todo_list.add_task("Task 1") 
        self.todo_list.remove_task("Task 1") 
        self.assertEqual(self.todo_list.tasks, []) 
 
if __name__ == '__main__': 
    unittest.main()