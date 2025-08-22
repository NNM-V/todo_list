import tkinter as tk
import json
import os

class JsonManager:
    def __init__(self,task_file):
        self.task_file = task_file
        if not os.path.exists(self.task_file):
            with open(self.task_file, "w") as f:
                json.dump([], f, indent=2)

    def load_task(self):
        with open(self.task_file,'r') as f:
            return json.load(f)

    def write_task(self,tasks):
        with open(self.task_file, "w") as f:
            json.dump(tasks, f, indent=2)