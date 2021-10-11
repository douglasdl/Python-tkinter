import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")

frame_entry = tk.Frame(master=window)
entry_temperature = tk.Entry(master=frame_entry, width=10)
label_temperature = tk.Label(master=frame_entry, text="\N{DEGREE FAHRENHEIT}")

entry_temperature.grid(row=0, column=0, sticky="e")
label_temperature.grid(row=0, column=1, sticky="w")

button_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}"
)
label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frame_entry.grid(row=0, column=0, padx=10)
button_convert.grid(row=0, column=1, pady=10)
label_temperature.grid(row=0, column=2, padx=10)

window.mainloop()