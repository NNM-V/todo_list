import tkinter as tk
from main_window import MainWindow

def main():
    root = tk.Tk()
    MainWindow(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()
