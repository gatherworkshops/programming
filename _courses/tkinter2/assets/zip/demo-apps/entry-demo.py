import tkinter

def entry_is_valid():
    return false

window = tkinter.Tk()
window.title("Entry Demo")
window.geometry("300x300")

entry = tkinter.Entry(window)
entry.config(width=20)
entry.config(validatecommand=entry_is_valid)
entry.config(validate=tkinter.focusout)
entry.grid()

window.mainloop()