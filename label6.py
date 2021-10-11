import tkinter as tk

window = tk.Tk()
window.title("Teste")

label = tk.Label(text="Name")
entry = tk.Entry()

label.pack()
entry.pack()

#Retrieve Text
name = entry.get()

#Delete Text
entry.delete(0)
entry.delete(0, 4)
entry.delete(0, tk.END)

#Insert Text
entry.insert(0, "Python")

window.mainloop()