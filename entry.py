import tkinter as tk

window = tk.Tk()
window.title("Teste")

label = tk.Label(
    text="Click me!",
    fg="white",
    bg="#24A24E",
    width=25,
    height=5
)
label.pack()
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

window.mainloop()