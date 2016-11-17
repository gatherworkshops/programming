import tkinter
from tkinter import messagebox

def validate_entry(event):
    entry_text = entry.get()
    error = None

    # make sure the text is longer than 3 characters
    if(len(entry_text) < 3):
        error = "Length must be greater than 3 letters"
    
    if error != None:

        popup_title = "Input Error"
        popup_text = error

        messagebox.showwarning(popup_title, popup_text)
    
    else:

        popup_title = "Thanks!"
        popup_text = "Thank you for your submission"

        messagebox.showinfo(popup_title, popup_text)



window = tkinter.Tk()
window.title("Entry Demo")
window.geometry("300x300")

entry = tkinter.Entry(window)
entry.config(width=20)
entry.bind("<Return>", validate_entry)
entry.grid()

button = tkinter.Button(window)
button.config(text="Submit")
button.bind("<ButtonPress>", validate_entry)
button.grid()

window.mainloop()