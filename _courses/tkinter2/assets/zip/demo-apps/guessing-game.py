import tkinter
import random

# VARIABLES #################

secret_number = None

# FUNCTIONALITY #############

def setup_game():
    generate_secret_number()


def generate_secret_number():
    '''
    Generates a secret random number between 
    1 and 10 that the user will have to guess.
    '''
    global secret_number

    secret_number = random.randint(1, 10)
    print("The secret number is", secret_number)



def check_guess(event):
    
    # get the user's guess from the entry
    text_guess = guess_entry.get()

    try:
        guess = int(text_guess)

        if guess == secret_number:
            feedback_label.config(text="You win! Woo!")
        elif guess < 1:
            feedback_label.config(text="Out of bounds, guess between 1 and 10")
        elif guess > 10:
            feedback_label.config(text="Out of bounds, guess between 1 and 10")
        elif guess < secret_number:
            feedback_label.config(text="Too low")
        elif guess > secret_number:
            feedback_label.config(text="Too high")

    except Exception:
        print("Not a number")

    

        


    
    
    
    


# INTERFACE #############

# Create the base window
window = tkinter.Tk()

# Create a label for displaying user feedback
feedback_label = tkinter.Label(window)
feedback_label.config(text="Guess a number between 1 and 10")
feedback_label.grid()

# Create an entry for the user's guess
guess_entry = tkinter.Entry(window)
guess_entry.bind("<Return>", check_guess)
guess_entry.grid()

# Create a submit button to check the guess
submit_button = tkinter.Button(window)
submit_button.config(text="Guess")
submit_button.bind("<Button>", check_guess)
submit_button.grid()

# Setup the game on first run
setup_game()

# Start the window's animation loop
window.mainloop()