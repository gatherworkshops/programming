import tkinter
window = tkinter.Tk()

window.title("Label Demo")
window.geometry("300x300")

label = tkinter.Label(window)
label.config(text="Hello")
label.config(font=("ComicSans", 22, "bold", "italic"))
label.config(foreground="red")
label.grid()

multiline_label = tkinter.Label(window)
multiline_label.config(text="Really long text that goes over more than one line to demonstrate how we do multi-line text in a label.")
multiline_label.config(wraplength=200)
multiline_label.config(justify="left")
multiline_label.config(padx=20, pady=10)
multiline_label.grid()

window.mainloop()