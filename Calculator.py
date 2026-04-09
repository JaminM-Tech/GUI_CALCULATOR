import tkinter as tk              # Import tkinter for GUI
import math                       # Import math module for scientific functions

# ─────────────────────────────────────────────
# CREATE MAIN WINDOW
# ─────────────────────────────────────────────
root = tk.Tk()                   
root.title("Scientific Calculator")  
root.geometry("380x520")         # ✅ Increased width so buttons fit properly
root.resizable(False, False)     
root.configure(bg="#1e1e1e")     

# Configure grid so ALL rows/columns expand evenly
for i in range(8):   # 8 rows total
    root.grid_rowconfigure(i, weight=1)

for j in range(4):   # 4 columns total
    root.grid_columnconfigure(j, weight=1)

# ─────────────────────────────────────────────
# ENTRY FIELD (DISPLAY SCREEN)
# ─────────────────────────────────────────────
entry = tk.Entry(
    root,
    font=("Arial", 22),
    bd=8,
    justify="right",
    bg="#2d2d2d",
    fg="white"
)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# ─────────────────────────────────────────────
# BASIC FUNCTIONS
# ─────────────────────────────────────────────

def click(value):
    """Insert value into the calculator display"""
    entry.insert(tk.END, value)

def clear():
    """Clear the entire display"""
    entry.delete(0, tk.END)

def backspace():
    """Remove last character"""
    entry.delete(len(entry.get()) - 1)

def equal():
    """Evaluate the mathematical expression"""
    try:
        expression = entry.get()
        expression = expression.replace("^", "**")  # Convert power symbol
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ─────────────────────────────────────────────
# SCIENTIFIC FUNCTIONS
# ─────────────────────────────────────────────

def sin_func():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def cos_func():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def tan_func():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def log_func():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sqrt_func():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def pi_func():
    entry.insert(tk.END, str(math.pi))

def e_func():
    entry.insert(tk.END, str(math.e))

# ─────────────────────────────────────────────
# KEYBOARD SUPPORT (FIXED)
# ─────────────────────────────────────────────

def key_event(event):
    key = event.char

    if key in "0123456789+-*/.":
        click(key)
        return "break"   # Prevent double input

    elif key == "\r":   # Enter key
        equal()
        return "break"

    elif event.keysym == "BackSpace":
        backspace()
        return "break"

root.bind("<Key>", key_event)

# ─────────────────────────────────────────────
# BUTTON DESIGN SETTINGS
# ─────────────────────────────────────────────
btn_bg = "#333"
btn_fg = "white"
btn_active = "#555"

def create_button(text, row, col, command):
    """Create and place a button in the grid"""
    tk.Button(
        root,
        text=text,
        font=("Arial", 14),
        bg=btn_bg,
        fg=btn_fg,
        activebackground=btn_active,
        command=command
    ).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# ─────────────────────────────────────────────
# STANDARD BUTTONS (ARITHMETIC INCLUDED)
# ─────────────────────────────────────────────
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == "=":
        create_button(text, row, col, equal)
    else:
        create_button(text, row, col, lambda x=text: click(x))

# ─────────────────────────────────────────────
# EXTRA FUNCTION BUTTONS
# ─────────────────────────────────────────────

create_button("C", 5, 0, clear)
create_button("⌫", 5, 1, backspace)
create_button("%", 5, 2, lambda: click("/100"))
create_button("^", 5, 3, lambda: click("^"))

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