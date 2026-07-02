import tkinter as tk
from tkinter import ttk
import json
from json_manager import JsonManager

COMPLETED_FILE = "completed_task.json"

class SubWindow(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)

        # create window
        self.title("Completed Tasks")
        self.geometry("400x300")
        self.completed_manager = JsonManager(COMPLETED_FILE)
        self.completed = self.completed_manager.load_task()
        self.create_widgets()

    def create_widgets(self):
        #Competed task frame
        completed_frame = tk.Frame(self)
        #create widget
        self.listbox = tk.Listbox(completed_frame, width=40, height=10, selectmode="multiple")
        scrollbar = tk.Scrollbar(completed_frame, orient='vertical', command=self.listbox.yview)
        #set scrollbar
        self.listbox['yscrollcommand'] = scrollbar.set
        #set widget
        self.listbox.pack(side='left')
        scrollbar.pack(side='right', fill='y')
        #set frame
        completed_frame.pack(padx=5, pady=20)

        #Button frame
        btn_frame = tk.Frame(self)
        #create widget
        clear_all_btn = ttk.Button(btn_frame,text="clear", width=11, command=self.clear_all_completed)
    
        #set widget
        clear_all_btn.pack(side='left', padx=(0,2))
        clear_all_btn.pack(side='left', padx=2)

        btn_frame.pack(side='top')

    def update_completed(self):
        self.listbox.delete(0,tk.END)

        for update_completed in self.completed:
            self.listbox.insert(tk.END,update_completed)

    def clear_all_completed(self):
        self.completed.clear()
        self.completed_manager.write_task(self.completed)
        self.update_completed()
        