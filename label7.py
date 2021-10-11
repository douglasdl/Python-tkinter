import tkinter as tk

window = tk.Tk()

label = tk.Label(text="Hello")
label.pack()

# Retrieve a Label's text
text = label["text"]

# Set new text for the label
label["text"] = "Good bye"

print(text)

window.mainloop()