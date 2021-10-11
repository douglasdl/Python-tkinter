import tkinter as tk

window = tk.Tk()
window.title("Teste")

text_box = tk.Text()
text_box.pack()

text_box.insert("1.0", "Hello") # line.character
text_box.insert("2.0", "World")
text_box.insert("2.0", "\nWorld")
text_box.insert(tk.END, "Text in the end.")
text_box.insert(tk.END, "\nText in the end (new line).")

window.mainloop()