import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("420x600")
root.resizable(0, 0)
root.config(bg="#1e1e1e")

# Global variable for storing expressions
expression = ""

# Function to update expression in the text entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    equation.set("")

# Scientific function definitions
def square_root():
    try:
        global expression
        result = str(math.sqrt(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def square():
    try:
        global expression
        result = str(float(expression) ** 2)
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def log():
    try:
        global expression
        result = str(math.log10(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def sin():
    try:
        global expression
        result = str(math.sin(math.radians(float(expression))))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def cos():
    try:
        global expression
        result = str(math.cos(math.radians(float(expression))))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def tan():
    try:
        global expression
        result = str(math.tan(math.radians(float(expression))))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Set up the GUI layout
equation = tk.StringVar()
entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 24), bg="#292929", fg="white", bd=8, width=17, borderwidth=0, justify="right")
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Style settings for buttons
button_style = {
    'font': ('Arial', 14, 'bold'),
    'bg': '#333333',
    'fg': 'white',
    'activebackground': '#4c4c4c',
    'activeforeground': 'white',
    'width': 5,
    'height': 2,
    'bd': 0,
    'relief': 'ridge'
}

# Create a function to make button widgets easily
def create_button(text, row, col, command=None, columnspan=1, custom_style=None):
    style = button_style.copy()
    if custom_style:
        style.update(custom_style)
    btn = tk.Button(root, text=text, command=command if command else lambda: press(text), **style)
    btn.grid(row=row, column=col, columnspan=columnspan, padx=5, pady=5, sticky="nsew")
    return btn

# Define the layout for numeric and operator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3)
]

for (text, row, col) in buttons:
    create_button(text, row, col)

# Clear and Equals buttons with custom styles
create_button('C', 4, 2, command=clear, custom_style={'bg': '#ff5c5c', 'fg': 'white', 'activebackground': '#ff7878'})
create_button('=', 5, 2, command=equalpress, columnspan=2, custom_style={'bg': '#007acc', 'fg': 'white', 'width': 12, 'activebackground': '#66b2ff'})

# Scientific functions with custom colors
create_button('√', 1, 4, command=square_root, custom_style={'bg': '#5e5e5e'})
create_button('x²', 2, 4, command=square, custom_style={'bg': '#5e5e5e'})
create_button('log', 3, 4, command=log, custom_style={'bg': '#5e5e5e'})
create_button('sin', 4, 4, command=sin, custom_style={'bg': '#5e5e5e'})
create_button('cos', 5, 3, command=cos, custom_style={'bg': '#5e5e5e'})
create_button('tan', 5, 4, command=tan, custom_style={'bg': '#5e5e5e'})

# Run the main loop
root.mainloop()
