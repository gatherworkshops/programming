import tkinter
import random


# APP FUNCTIONALITY ***************

def say_hello(event):
    print("Why hello there!")

def generate_random_number(event):
    number = random.randint(1, 10)
    random_label.config(text=number)

# APP INTERFACE *******************

window = tkinter.Tk()

window.title("Button Demo")
window.geometry("300x300")

button = tkinter.Button(window)
button.config(text="Click Me!")
button.bind("<Button>", say_hello)
button.grid()

random_label = tkinter.Label(window)
random_label.config(text="No number yet :(")
random_label.grid()

random_button = tkinter.Button(window)
random_button.config(text="Generate Random Number")
random_button.bind("<Button>", generate_random_number)
random_button.grid()

disabled_button = tkinter.Button(window)
disabled_button.config(text="Unclickable")
disabled_button.config(state=tkinter.DISABLED)
disabled_button.grid()

window.mainloop()