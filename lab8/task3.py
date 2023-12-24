import tkinter as tk
from tkinter import messagebox, StringVar, ttk


def submit_ticket():
    name = name_entry.get()
    destination = destination_var.get()
    flight_time = flight_time_var.get()
    drinks = ", ".join([drink for drink, var in drinks_vars.items() if var.get()])

    if not name or not destination or not flight_time or not drinks:
        messagebox.showinfo("Incomplete Information", "Please fill in all fields.")
        return

    ticket_info.config(
        text=f"Your ticket:\nName: {name}\nDestination: {destination}\n"
        f"Flight Time: {flight_time}\nDrinks: {drinks}",
        fg="green",
    )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("New Ticket")

    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Destination").pack()
    destination_var = StringVar()
    destination_dropdown = ttk.Combobox(
        root,
        textvariable=destination_var,
        values=["Kuwait", "Bahrain", "Qatar", "UAE", "Oman"],
    )
    destination_dropdown.pack()

    tk.Label(root, text="Preferred flight time").pack()
    flight_time_var = StringVar()
    tk.Radiobutton(
        root, text="Morning", variable=flight_time_var, value="Morning"
    ).pack()
    tk.Radiobutton(
        root, text="Evening", variable=flight_time_var, value="Evening"
    ).pack()

    tk.Label(root, text="Preferred drinks on the plane:").pack()
    drinks_vars = {
        "coffee": tk.BooleanVar(),
        "tea": tk.BooleanVar(),
        "water": tk.BooleanVar(),
    }
    for drink, var in drinks_vars.items():
        tk.Checkbutton(root, text=drink, variable=var).pack()

    submit_button = tk.Button(root, text="Submit", command=submit_ticket)
    submit_button.pack()

    ticket_info = tk.Label(root, text="")
    ticket_info.pack()

    root.mainloop()
