import tkinter as tk

window = tk.Tk()
window.title("Teste")

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",
    background="black"    
)
label.pack()

window.mainloop()