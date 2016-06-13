import tkinter
import random

FRUIT_OPTIONS = ["Orange", "Apple", "Banana", "Pear", "Jalapeno"]

window = tkinter.Tk()


# prints "hello" in the developer console
def say_hello(event):
    name = name_entry.get()

    if len(name) > 0:
        print("Hello, " + name + "!")
    else:
        print("Hello random stranger!")


# adds a random fruit to the fruit list,
# only allowing a maximum of 8 fruit
def add_fruit(event):

    if fruit_list.size() >= 8:
        return

    random_index = random.randrange(0, len(FRUIT_OPTIONS))
    random_fruit = FRUIT_OPTIONS[random_index]
    fruit_list.insert(tkinter.END, random_fruit)


# deletes the selected fruit from the list,
# if one is selected
def delete_fruit(event):
    selected_fruit = fruit_list.curselection()
    fruit_list.delete(selected_fruit)


# generates a smoothie recipe from the fruit
# selection made by the user
def generate_recipe(event):
    fruit_counter = {}

    # count the number of each type of fruit
    # using a dictionary
    chosen_fruit = fruit_list.get(0, tkinter.END)
    for fruit in chosen_fruit:
        if fruit in fruit_counter:
            fruit_counter[fruit] += 1
        else :
            fruit_counter[fruit] = 1

    # generate recipe text using the dictionary
    recipe_text = "Recipe:\n\n"

    for fruit_type in fruit_counter:
        recipe_line = str(fruit_counter[fruit_type]) + " x " + fruit_type + "\n"
        recipe_text += recipe_line

    # delete the old recipe if there was one
    recipe_display.delete("1.0", tkinter.END)

    # display the new recipe
    recipe_display.insert(tkinter.END, recipe_text)


# name prompt
name_prompt = tkinter.Label(window)
name_prompt.config(text="What is your name?")
name_prompt.grid(row=0, column=0)

# name input
name_entry = tkinter.Entry(window)
name_entry.grid(row=1, column=0)

# hello button
hello_button = tkinter.Button(window)
hello_button.config(text="Click Me!")
hello_button.grid(row=2, column=0)

# fruit list
fruit_list = tkinter.Listbox(window)
fruit_list.grid(row=0, column=1, columnspan=2, sticky="nesw")

# add fruit button
add_fruit_button = tkinter.Button(window)
add_fruit_button.config(text="Add Random Fruit")
add_fruit_button.grid(row=1, column=1, sticky="ew")

# delete fruit button
delete_fruit_button = tkinter.Button(window)
delete_fruit_button.config(text="Delete Fruit")
delete_fruit_button.grid(row=1, column=2, sticky="ew")

# recipe button
create_recipe_button = tkinter.Button(window)
create_recipe_button.config(text="Generate Recipe")
create_recipe_button.grid(row=1, column=3)

# recipe display
recipe_display = tkinter.Text(window)
recipe_display.grid(row=0, column=3)

window.mainloop()
