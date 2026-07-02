import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import json
import datetime

from json_manager import JsonManager
from sub_window import SubWindow

TASK_FILE = "task.json"
COMPLETED_FILE = "completed_task.json"

class MainWindow(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        #create window
        master.title('ToDo App')
        master.geometry('600x400')
        self.saved = True
        master.protocol('WM_DELETE_WINDOW', self.delete_window)
        self.sub_win = None
        self.task_manager = JsonManager(TASK_FILE)
        self.completed_manager = JsonManager(COMPLETED_FILE)
        self.tasks = self.task_manager.load_task()
        self.completed = self.completed_manager.load_task()
        self.create_widgets()

    def delete_window(self):
        if not self.saved:
            ret = messagebox.askyesno('Warning', 'Do you want exit without saving?',icon='question')
            if ret:
                self.master.destroy()
            else:
                return
        else:
            self.master.destroy()

    def create_widgets(self):
        #Entry frame
        entry_frame = tk.Frame(self, padx=5, pady=10, bd=2)
        #create widget 
        entry_label = tk.Label(entry_frame, text='Input task:')
        self.entry = tk.Entry(entry_frame, width=27) 
        add_btn = tk.Button(entry_frame,text='add', command=self.add_task)
        #set widget
        entry_label.pack(side=tk.LEFT, padx=(5,0))
        self.entry.pack(side=tk.LEFT)
        add_btn.pack(side=tk.LEFT, padx=5)
        #set frame
        entry_frame.pack()

        task_label = tk.Label(self, text='Todo:', width=10, anchor=tk.W)
        task_label.pack(padx=10, anchor=tk.W)

        #Task frame
        task_frame = tk.Frame(self)
        #create widget
        self.listbox = tk.Listbox(task_frame, width=40, height=10, selectmode='multiple')
        scrollbar = tk.Scrollbar(task_frame, orient='vertical', command=self.listbox.yview)
        #set scrollbar
        self.listbox['yscrollcommand'] = scrollbar.set
        #set widget
        self.listbox.pack(side='left')
        scrollbar.pack(side='right', fill='both')
        #set frame
        task_frame.pack(side=tk.TOP, pady=10)

        #Button frame
        btn_frame = tk.Frame(self)
        #create widget
        select_all_btn = ttk.Button(btn_frame,text='select all', width=11, command=self.selectall_task)
        deselect_all_btn = ttk.Button(btn_frame,text='deselect', command=self.deselect_task)
        complete_btn = ttk.Button(btn_frame,text='complete', command=self.complete_task)
    
        #set widget
        select_all_btn.pack(side='left', padx=(0,2))
        deselect_all_btn.pack(side='left', padx=2)
        complete_btn.pack(side='left', padx=2)

        btn_frame.pack(side=tk.TOP)

        #Button frame2
        btn_frame2 = tk.Frame(self)

        style = ttk.Style()
        style.configure('Del.TButton', foreground='red')

        new_win_btn = ttk.Button(btn_frame2, text='show completed', width=11, command=self.show_subwindow)
        save_btn = ttk.Button(btn_frame2,text='save', command=self.save_task)
        delete_btn = ttk.Button(btn_frame2, text='delete', style='Del.TButton', command=self.delete_task)
        
        new_win_btn.pack(side='left', padx=(0,2))
        save_btn.pack(side='left', padx=2)
        delete_btn.pack(side='left', padx=2)

        btn_frame2.pack(side=tk.TOP)
        
    def update_task(self):
        self.listbox.delete(0,tk.END)

        for update_task in self.tasks:
            self.listbox.insert(tk.END,update_task)

    def add_task(self):
        new_task = self.entry.get()

        if new_task:
            self.tasks.append(new_task)
            self.update_task()
            self.entry.delete(0,tk.END)
            self.saved = False

    def selectall_task(self):
        self.listbox.select_set(0,tk.END)

    def deselect_task(self):
        self.listbox.select_clear(0,tk.END)
    
    def complete_task(self):
        selectedIndex = self.listbox.curselection()

        for i in reversed(selectedIndex):
            selected_task = self.listbox.get(i)
            time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            completed_task = {"task": selected_task,"Time completed": time}
            self.completed.append(completed_task)
            self.listbox.delete(i)
            del self.tasks[i]

        self.update_task()

        if self.sub_win is not None and self.sub_win.winfo_exists():
            self.sub_win.completed = self.completed 
            self.sub_win.update_completed()

        self.saved = False

    def save_task(self):
        self.task_manager.write_task(self.tasks)
        self.completed_manager.write_task(self.completed)
        self.saved = True

    def delete_task(self):
        ret = messagebox.askyesno('Warning', 'Do you want to delete tasks?',icon='question')
        if ret:
            selectedIndex = self.listbox.curselection()

            for i in reversed(selectedIndex):
                self.listbox.delete(i)
                del self.tasks[i]

            self.update_task()
            self.task_manager.write_task(self.tasks)
            self.saved = False

        else:
            return

    def show_subwindow(self):
       if self.sub_win is None or not self.sub_win.winfo_exists():
            self.sub_win = SubWindow(self.master)
            self.sub_win.completed = self.completed 
            self.sub_win.update_completed()
