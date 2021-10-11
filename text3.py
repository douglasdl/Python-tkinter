import tkinter as tk

window = tk.Tk()
window.title("Teste")

text_box = tk.Text()
text_box.pack()

text_box.delete("1.0") # line.character
text_box.delete("1.0", "1.5")
text_box.delete("1.0", tk.END)

window.mainloop()