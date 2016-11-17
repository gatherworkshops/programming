import tkinter

people = []



# FUNCTIONALITY ##########################

def create_people():
    
    marge = Person("Marge", "Simpson", '045678900')
    people.append(marge)

    homer = Person("Homer", "Simpson", '045678900')
    people.append(homer)



def update_list_items():

    # remove all items in the listbox
    listbox.delete(0, tkinter.END)

    # add each person's full name to the list
    for person in people:
        name = person.first_name + ' ' + person.last_name
        listbox.insert(tkinter.END, name)



def display_selected_item(event):

    # get the item
    selected_index = listbox.curselection()[0]
    selected_person = people[selected_index]

    # display the item info
    label.config(text=selected_person.first_name)


create_people()
update_list_items()


# INTERFACE ################################

window = tkinter.Tk()

listbox = tkinter.Listbox(window)
listbox.bind("<Double-Button>", display_selected_item)
listbox.grid()
update_list_items()

label = tkinter.Label(window)
label.config(text="Hello")
label.grid()

window.mainloop()



# CLASSES ####################################

class Person(object):
    
    first_name = None
    last_name = None
    number = 0

    def __init__(self, first_name, last_name, phone):
        this.first_name = first_name
        this.last_name = last_name
        this.phone = phone
