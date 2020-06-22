import tkinter as tk
from tkinter import simpledialog
def name(a):
    return('Hello',a)
na=tk.Tk()
na.withdraw()
me=simpledialog.askstring(title='Test',prompt="What's Your Name:")
print(name(me))
