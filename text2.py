import tkinter as tk

window = tk.Tk()
window.title("Teste")

text_box = tk.Text()
text_box.pack()

text_box.get("1.0") # line.character
text_box.get("1.0", "1.5")
text_box.get("2.0", "2.5")
text_box.get("1.0", tk.END)

window.mainloop()