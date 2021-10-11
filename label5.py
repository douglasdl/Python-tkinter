import tkinter as tk

window = tk.Tk()
window.title("Teste")

label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="#34A2FE",
    width=10,
    height=10
)
label.pack()

window.mainloop()