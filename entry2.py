import tkinter as tk

window = tk.Tk()
window.title("Teste")

label = tk.Label(text="Name")
entry = tk.Entry()

label.pack()
entry.pack()

window.mainloop()