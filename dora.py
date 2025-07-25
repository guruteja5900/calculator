import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Global variable for the expression
expression = ""

# Function to update expression
def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

# Function to evaluate the expression
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result  # allow chaining operations
    except Exception:
        input_text.set("Error")
        expression = ""

# Function to clear input
def clear():
    global expression
    expression = ""
    input_text.set("")

# Display frame
input_text = tk.StringVar()
input_frame = tk.Entry(root, textvariable=input_text, font=('Arial', 20), bd=10, justify='right')
input_frame.pack(fill='both', ipadx=8, ipady=8, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for row_values in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')
    for val in row_values:
        if val == '=':
            btn = tk.Button(frame, text=val, font=('Arial', 18), fg="white", bg="green", command=evaluate)
        elif val == 'C':
            btn = tk.Button(frame, text=val, font=('Arial', 18), fg="white", bg="red", command=clear)
        else:
            btn = tk.Button(frame, text=val, font=('Arial', 18), command=lambda v=val: press(v))
        btn.pack(side='left', expand=True, fill='both')

root.mainloop()
