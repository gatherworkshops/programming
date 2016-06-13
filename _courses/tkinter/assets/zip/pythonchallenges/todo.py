import tkinter

# =====
# CLASSES
# =====

# No classes yet


# =====
# CONSTANTS
# =====

APP_TITLE_TEXT = "Things To Do"
SAMPLE_TODO_TEXT = "This is a sample to-do item"
NEW_TODO_PROMPT = "I also need to..."


# =====
# VARIABLES
# =====

# No variables yet


# =====
# FUNCTIONALITY
# =====


def remove_selected_item(event):
    print("remove selected item from list")


def add_new_item(event):
    print("add new item to list")


# =====
# WIDGETS
# =====

# WINDOW
# Create the app window
window = tkinter.Tk()
window.minsize(350, 450)
window.title(APP_TITLE_TEXT)

# HEADING
# Display the name of the app in large text
title_label = tkinter.Label(window)
title_label.config(text=APP_TITLE_TEXT, font="Verdana 24 bold", fg="white", bg="gray6", pady=10)
title_label.grid(row=0, column=0, sticky="ew", columnspan=2)

# LIST
# Show a list of all the things still to do
todo_list = tkinter.Listbox(window)
todo_list.config(borderwidth=0, bg="white", font="ComicSansMS 16 bold", selectbackground="LightGoldenrod1")
todo_list.insert(0, SAMPLE_TODO_TEXT)
todo_list.grid(row=1, column=0, sticky="nesw")

# DONE BUTTON
# Allows the user to remove a to-do item from the list
done_button = tkinter.Button(window)
done_button.config(text="Done it!", borderwidth=0)
done_button.grid(row=2, column=0, sticky="ew")

# NEW TO-DO PANEL
# Put the new to-do in a panel that the padding
# and background colours can be easily set
new_todo_panel = tkinter.Frame(window)
new_todo_panel.config(padx=20, pady=20, bg="PaleGreen1")
new_todo_panel.grid(row=3, column=0, sticky="nesw")

# NEW TO-DO PROMPT
# Tells the user they can create a new to-do using the entry box
prompt_label = tkinter.Label(new_todo_panel)
prompt_label.config(text=NEW_TODO_PROMPT, bg="PaleGreen1")
prompt_label.grid(row=3, column=0, sticky="w")

# NEW TO-DO ENTRY
# The user can type in here to make a new to-do
todo_entry = tkinter.Entry(new_todo_panel)
todo_entry.config(bg="white")
todo_entry.grid(row=4, column=0, sticky="ew")

# NEW TO-DO SAVE BUTTON
# Allows the user to add their new entry to the to-do list
save_button = tkinter.Button(new_todo_panel)
save_button.config(text="Save New To-Do", bg="PaleGreen1")
save_button.grid(row=5, column=0, sticky="e", pady=5, padx=5)

# COLUMN SIZING
# Grow the grid to match the window width
window.columnconfigure(0, weight=1)
new_todo_panel.columnconfigure(0, weight=1)

# ROW SIZING
# Grow the list section to fill any extra space
window.rowconfigure(1, weight=1)

# run the GUI
window.mainloop()
