import tkinter as tk
from tkinter import ttk
from functools import partial

# Function to handle button clicks (adding values to the entry)
def button_click(value):
    current = entry.get()  # Get the current text in the entry
    entry.delete(0, tk.END)  # Clear the entry
    entry.insert(tk.END, current + value)  # Append the clicked value

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)  # Clear the text in the entry

# Function to perform the calculation
def calculate():
    try:
        result = eval(entry.get())  # Evaluate the expression in the entry
        entry.delete(0, tk.END)  # Clear the entry
        entry.insert(tk.END, str(result))  # Insert the result
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # Show error if the calculation fails

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget to display input and output
entry = tk.Entry(root, font=('Helvetica', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Creating each button manually and linking them to the corresponding functions
button_7 = ttk.Button(root, text="7", command=partial(button_click, '7'))
button_7.grid(row=1, column=0, padx=5, pady=5)

button_8 = ttk.Button(root, text="8", command=partial(button_click, '8'))
button_8.grid(row=1, column=1, padx=5, pady=5)

button_9 = ttk.Button(root, text="9", command=partial(button_click, '9'))
button_9.grid(row=1, column=2, padx=5, pady=5)

button_divide = ttk.Button(root, text="/", command=partial(button_click, '/'))
button_divide.grid(row=1, column=3, padx=5, pady=5)

button_4 = ttk.Button(root, text="4", command=partial(button_click, '4'))
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = ttk.Button(root, text="5", command=partial(button_click, '5'))
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = ttk.Button(root, text="6", command=partial(button_click, '6'))
button_6.grid(row=2, column=2, padx=5, pady=5)

button_multiply = ttk.Button(root, text="*", command=partial(button_click, '*'))
button_multiply.grid(row=2, column=3, padx=5, pady=5)

button_1 = ttk.Button(root, text="1", command=partial(button_click, '1'))
button_1.grid(row=3, column=0, padx=5, pady=5)

button_2 = ttk.Button(root, text="2", command=partial(button_click, '2'))
button_2.grid(row=3, column=1, padx=5, pady=5)

button_3 = ttk.Button(root, text="3", command=partial(button_click, '3'))
button_3.grid(row=3, column=2, padx=5, pady=5)

button_minus = ttk.Button(root, text="-", command=partial(button_click, '-'))
button_minus.grid(row=3, column=3, padx=5, pady=5)

button_0 = ttk.Button(root, text="0", command=partial(button_click, '0'))
button_0.grid(row=4, column=0, padx=5, pady=5)

button_dot = ttk.Button(root, text=".", command=partial(button_click, '.'))
button_dot.grid(row=4, column=1, padx=5, pady=5)

button_equals = ttk.Button(root, text="=", command=calculate)
button_equals.grid(row=4, column=2, padx=5, pady=5)

button_plus = ttk.Button(root, text="+", command=partial(button_click, '+'))
button_plus.grid(row=4, column=3, padx=5, pady=5)

# Create the clear button
clear_button = ttk.Button(root, text="C", command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Start the main loop to run the application
root.mainloop()
