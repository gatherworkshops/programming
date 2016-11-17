import tkinter

# VARIABLES ########################

contacts = []


# CLASSES ##########################

class Contact:
    name = None
    phone = None

    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone


# FUNCTIONALITY ####################

def setup_app():
    '''
    Sets up any variables or settings we need
    at the start of the program
    '''

    # create sample contacts
    fred = Contact("Fred Flintstone", "04567890")
    contacts.append(fred)

    scooby = Contact("Scooby Doo")
    contacts.append(scooby)

    update_contact_listbox()


def update_contact_listbox():
    '''
    Takes the list of contacts and adds each
    one's name to the listbox in the UI
    '''
    contact_list.delete(0, tkinter.END)

    for contact in contacts:
        contact_string = contact.name + '(' + (contact.phone or " ") + ')'
        contact_list.insert(tkinter.END, contact_string)


def create_contact(event):
    name = name_entry.get()
    phone = phone_entry.get()

    new_contact = Contact(name, phone)
    contacts.append(new_contact)

    update_contact_listbox()


def delete_contact(event):
    selected_index = contact_list.curselection()[0]
    selected_index = int(selected_index)

    contacts.pop(selected_index)

    update_contact_listbox()


# INTERFACE ########################
window = tkinter.Tk()

# app title
title = tkinter.Label(window)
title.config(text="Contact Manager")
title.config(font=("Verdana", 18, "bold"))
title.grid(row=0, column=0, columnspan=2, sticky="w")

# contact list
contact_list = tkinter.Listbox(window)
contact_list.grid(row=1, column=0, columnspan=2, sticky="ew")

# name label
name_label = tkinter.Label(window)
name_label.config(text="Name")
name_label.grid(row=2, column=0, sticky="w")

# name entry
name_entry = tkinter.Entry(window)
name_entry.grid(row=3, column=0)

# phone label
phone_label = tkinter.Label(window)
phone_label.config(text="Phone")
phone_label.grid(row=2, column=1, sticky="w")

# phone entry
phone_entry = tkinter.Entry(window)
phone_entry.grid(row=3, column=1)

# save button
save_button = tkinter.Button(window)
save_button.config(text="Save")
save_button.bind("<Button>", create_contact)
save_button.grid(row=4, column=0, sticky="e", padx=5, pady=10)

# delete button
delete_button = tkinter.Button(window)
delete_button.config(text="Delete")
delete_button.bind("<Button>", delete_contact)
delete_button.grid(row=4, column=1, sticky="w",padx=5, pady=10)



setup_app()
window.mainloop()