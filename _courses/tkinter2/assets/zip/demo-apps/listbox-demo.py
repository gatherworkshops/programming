import tkinter



# VARIABLES ##############################

list_items = [
    "Zebra",
    "Dingo",
    "Cape Barren Goose",
    "Orangutan",
    "Sloth",
    "Red Panda"
]



# FUNCTIONALITY ##########################

def init_app():
    update_list()
    

def item_clicked(event):

    # get the item
    selected_index = listbox.curselection()[0]
    selected_person = people[selected_index]

    # display the item info
    label.config(text=selected_person.first_name)


def add_item(event):

    new_item = entry.get()
    entry.delete(0, tkinter.END)

    if len(new_item) > 0:
        list_items.append(new_item)
        update_list()


def delete_item(event):

    selected_index = listbox.curselection()[0]
    list_items.pop(selected_index)
    update_list()


def update_list():

    # remove all items in the listbox
    listbox.delete(0, tkinter.END)

    # add each item to the list
    for item in list_items:
        listbox.insert(tkinter.END, item)    


# INTERFACE ################################

window = tkinter.Tk()

listbox = tkinter.Listbox(window)
listbox.config(width=80) # in chars
listbox.config(height=12) # in chars
listbox.config(listvariable=list_items)
listbox.bind("<Double-Button>", item_clicked)
listbox.grid()

entry = tkinter.Entry(window)
entry.bind("<Return>", add_item)
entry.grid()

add_button = tkinter.Button(window)
add_button.config(text="Add")
add_button.bind("<Button>", add_item)
add_button.grid()

delete_button = tkinter.Button(window)
delete_button.config(text="Delete")
delete_button.bind("<Button>", delete_item)
delete_button.grid()


init_app()
window.mainloop()
