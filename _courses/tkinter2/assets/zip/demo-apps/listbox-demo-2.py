import tkinter

# VARIABLES #######################

animals = [
    "Puma",
    "Magpie",
    "Crocodile",
    "Ant",
    "Bunny"
] 

# FUNCTIONALITY #########################

def setup_app():
    update_listbox()

def update_listbox()

    # delete all items from listbox
    listbox.delete(0, tkinter.END)

    # Add all animals from our list
    for animal in animals:
        listbox.insert(tkinter.END, animal)

def add_new_item(event):
    # Get the animal from the text entry
    new_animal = entry.get()
    entry.delete(0, tkinter.END)

    # add it to our list of animals
    animals.append(new_animal)

    # Update the listbox to display the new animal
    update_listbox()



def delete_item(event):
    selected_index = listbox.curselection()[0]
    selected_index = int(selected_index)
    animals.pop(selected_index)
    update_listbox()



# INTERFACE #############################

# Create a base window
window = tkinter.Tk()

# Create a list to display the items
listbox = tkinter.Listbox(window)
listbox.config(width=80) # in chars
listbox.config(height=12) # in chars
listbox.grid()

# Create entry to add new items
entry = tkinter.Entry(window)
entry.bind("<Return>", add_new_item)
entry.grid()

# Button to submit the new item
add_button = tkinter.Button(window)
add_button.config(text="Add")
add_button.bind("<Button>", add_new_item)
add_button.grid()

# Button to delete items from the list
delete_button = tkinter.Button(window)
delete_button.config(text="Delete")
delete_button.bind("<Button>", delete_item)
delete_button.grid()

# Setup the app
setup_app()

# Start the visual app
window.mainloop()