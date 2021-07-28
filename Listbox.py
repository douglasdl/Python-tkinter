from tkinter import *
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

root = Tk()
root.title("Excel")
root.iconbitmap("favicon.ico")
root.geometry("300x300")

my_list = ["one", "two", "three"]

# Create Listbox
my_listbox = Listbox(root, width=45)
my_listbox.pack(pady=20)

# Load list to listbox
for item in my_list:
    my_listbox.insert(END, item)

root.mainloop()