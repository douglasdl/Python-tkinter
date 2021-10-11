import tkinter as tk

window = tk.Tk()
window.title("Icon Test")

window.iconphoto(False, tk.PhotoImage(file='favicon.png'))
#root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='favicon.ico')

window.mainloop()

# Close the Program
window.destroy()