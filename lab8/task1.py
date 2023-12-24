import tkinter as tk
import random


def check_guess():
    try:
        user_guess = int(entry.get())
        if user_guess == rand_number:
            result_label.config(text="You win!")
        elif user_guess < rand_number:
            result_label.config(text="Too low!")
        else:
            result_label.config(text="Too high!")
    except ValueError:
        result_label.config(text="Please enter a valid number.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Guess the Number")

    rand_number = random.randint(0, 10)

    entry = tk.Entry(root)
    entry.pack()

    guess_button = tk.Button(root, text="Guess", command=check_guess)
    guess_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()
