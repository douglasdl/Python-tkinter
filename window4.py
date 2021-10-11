import tkinter as tk

window = tk.Tk()
window.title("Teste")

label = tk.Label(text="Name")
label.pack()

window.mainloop()

# Close the Program
window.destroy()