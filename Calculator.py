import tkinter as tk              # Import tkinter for GUI
import math                       # Import math module for scientific functions

# ─────────────────────────────────────────────
# CREATE MAIN WINDOW
# ─────────────────────────────────────────────
root = tk.Tk()                   # Create main window
root.title("Scientific Calculator")  # Window title
root.geometry("350x500")         # Set window size
root.resizable(False, False)     # Disable resizing
root.configure(bg="#1e1e1e")     # Set background color

# ─────────────────────────────────────────────
# ENTRY FIELD (DISPLAY SCREEN)
# ─────────────────────────────────────────────
entry = tk.Entry(
    root,
    width=20,
    font=("Arial", 22),
    bd=8,
    justify="right",
    bg="#2d2d2d",
    fg="white"
)
entry.grid(row=0, column=0, columnspan=5, pady=10)

# ─────────────────────────────────────────────
# BASIC FUNCTIONS
# ─────────────────────────────────────────────

# Function to insert numbers/operators into display
def click(value):
    entry.insert(tk.END, value)

# Function to clear entire screen
def clear():
    entry.delete(0, tk.END)

# Function to delete last character (Backspace)
def backspace():
    entry.delete(len(entry.get()) - 1)

# Function to evaluate expression
def equal():
    try:
        expression = entry.get()

        # Replace power symbol ^ with Python's **
        expression = expression.replace("^", "**")

        # Evaluate the expression
        result = eval(expression)

        # Display result
        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ─────────────────────────────────────────────
# SCIENTIFIC FUNCTIONS
# ─────────────────────────────────────────────

# Each function gets value from entry, calculates, then displays result

def sin_func():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))  # Convert to radians
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def cos_func():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def tan_func():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def log_func():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

def sqrt_func():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

# Insert constant π
def pi_func():
    entry.insert(tk.END, str(math.pi))

# Insert constant e
def e_func():
    entry.insert(tk.END, str(math.e))

# ─────────────────────────────────────────────
# KEYBOARD SUPPORT
# ─────────────────────────────────────────────

def key_event(event):
    key = event.char

    # Allow numbers and operators
    if key in "0123456789+-*/.":
        click(key)

    # Enter key → calculate
    elif key == "\r":
        equal()

    # Backspace key → delete last character
    elif event.keysym == "BackSpace":
        backspace()

root.bind("<Key>", key_event)

# ─────────────────────────────────────────────
# BUTTON DESIGN SETTINGS
# ─────────────────────────────────────────────
btn_bg = "#333"
btn_fg = "white"
btn_active = "#555"

# Function to create buttons easily
def create_button(text, row, col, command):
    tk.Button(
        root,
        text=text,
        width=5,
        height=2,
        font=("Arial", 12),
        bg=btn_bg,
        fg=btn_fg,
        activebackground=btn_active,
        command=command
    ).grid(row=row, column=col, padx=5, pady=5)

# ─────────────────────────────────────────────
# STANDARD BUTTONS
# ─────────────────────────────────────────────
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

# Create standard buttons
for (text, row, col) in buttons:
    if text == "=":
        create_button(text, row, col, equal)
    else:
        create_button(text, row, col, lambda x=text: click(x))

# ─────────────────────────────────────────────
# EXTRA FUNCTION BUTTONS
# ─────────────────────────────────────────────

create_button("C", 5, 0, clear)               # Clear screen
create_button("⌫", 5, 1, backspace)          # Backspace
create_button("%", 5, 2, lambda: click("/100"))  # Percentage
create_button("^", 5, 3, lambda: click("^"))     # Power

# Scientific buttons
create_button("sin", 6, 0, sin_func)
create_button("cos", 6, 1, cos_func)
create_button("tan", 6, 2, tan_func)
create_button("log", 6, 3, log_func)

create_button("√", 7, 0, sqrt_func)
create_button("π", 7, 1, pi_func)
create_button("e", 7, 2, e_func)

# ─────────────────────────────────────────────
# RUN APPLICATION
# ─────────────────────────────────────────────
root.mainloop()