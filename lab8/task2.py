import tkinter as tk
from tkinter import messagebox


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")

    entry1 = tk.Entry(root)
    entry1.pack()

    entry2 = tk.Entry(root)
    entry2.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    calculator_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Calculator", menu=calculator_menu)

    calculator_menu.add_command(label="ADD", command=lambda: calculate("add"))
    calculator_menu.add_command(label="SUB", command=lambda: calculate("sub"))
    calculator_menu.add_command(label="MUL", command=lambda: calculate("mul"))
    calculator_menu.add_command(label="DIV", command=lambda: calculate("div"))

    root.mainloop()
