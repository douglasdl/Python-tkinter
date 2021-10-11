import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_textarea.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_textarea.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_textarea.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


# Set-up the window
window = tk.Tk()
window.title("Text Editor")
window.rowconfigure(0, minsize=400, weight=1) # First row (single row app)
window.columnconfigure(1, minsize=800, weight=1) # Second column

# Create the widgets
text_textarea = tk.Text(window)
frame_sidemenu = tk.Frame(window)
button_open = tk.Button(frame_sidemenu, text="Open", command=open_file)
button_save = tk.Button(frame_sidemenu, text="Save as...", command=save_file)

# Set-up the buttons layout using the .grid() geometry manager
button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button_save.grid(row=1, column=0, sticky="ew", padx=5)



# Set-up the layout using the .grid() geometry manager
frame_sidemenu.grid(row=0, column=0, sticky="ns")
text_textarea.grid(row=0, column=1, sticky="nsew")

# Run the application
window.mainloop()