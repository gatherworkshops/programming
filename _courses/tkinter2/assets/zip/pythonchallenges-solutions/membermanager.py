import tkinter
window = tkinter.Tk()
window.geometry("600x300")



# HEADING
# Create the main app heading label
title_label = tkinter.Label(window)
title_label.config(text="Super Duper Member Manager", font="Verdana 24 bold", bg="yellow")
title_label.grid(row=0, column=0, sticky="ew", columnspan=4)



# NEW MEMBERS
# Heading for the "New Member" section
new_member_label = tkinter.Label(window)
new_member_label.config(text="New Member", font="Verdana 16 bold")
new_member_label.grid(row=1, column=0, sticky="w", columnspan=3)

# Label for the "First Name" entry box
firstname_label = tkinter.Label(window)
firstname_label.config(text="First Name")
firstname_label.grid(row=2, column=0, sticky="w")

# Entry box for "First Name"
firstname_entry = tkinter.Entry(window)
firstname_entry.grid(row=2, column=1, sticky="ew", columnspan=2)

# Label for the "Last Name" entry box
lastname_label = tkinter.Label(window)
lastname_label.config(text="Last Name")
lastname_label.grid(row=3, column=0, sticky="w")

# Entry box for "Last Name"
lastname_entry = tkinter.Entry(window)
lastname_entry.grid(row=3, column=1, sticky="ew", columnspan=2)

# Label for the "Mobile" entry box
mobile_label = tkinter.Label(window)
mobile_label.config(text="Mobile")
mobile_label.grid(row=4, column=0, sticky="w")

# Entry box for "Mobile"
mobile_entry = tkinter.Entry(window)
mobile_entry.grid(row=4, column=1, sticky="ew", columnspan=2)

# Cancel button
cancel_button = tkinter.Button(window)
cancel_button.config(text="Cancel")
cancel_button.grid(row=6, column=1, sticky="ew")

# Save button
save_button = tkinter.Button(window)
save_button.config(text="Save")
save_button.grid(row=6, column=2, sticky="ew")



# ALL MEMBERS
# Heading for the "All Members" section
all_members_label = tkinter.Label(window)
all_members_label.config(text="All Members", font="Verdana 16 bold")
all_members_label.grid(row=1, column=3, sticky="w")

# List box to display member names
members_list_box = tkinter.Listbox(window)
members_list_box.grid(row=2, column=3, rowspan=5, sticky="nesw")


# COLUMN SIZING
# Grow all columns at the same rate,
# except column one which is a fixed width
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)


window.mainloop()