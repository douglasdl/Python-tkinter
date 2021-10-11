import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = entry_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    label_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# Set-up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frame_entry = tk.Frame(master=window)
entry_temperature = tk.Entry(master=frame_entry, width=10)
label_temperature = tk.Label(master=frame_entry, text="\N{DEGREE FAHRENHEIT}")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
entry_temperature.grid(row=0, column=0, sticky="e")
label_temperature.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
button_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Set-up the layout using the .grid() geometry manager
frame_entry.grid(row=0, column=0, padx=10)
button_convert.grid(row=0, column=1, pady=10)
label_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()