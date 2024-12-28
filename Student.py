from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
      