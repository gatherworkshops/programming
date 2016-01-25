# BURGER BUILDER
# Author: Tanya Gray, Gather Workshops

# The Burger Builder collects burger orders.
# Each burger order consists of a bottom bun
# and a top bun, but the contents can be
# added in any order.
#
# Each order must also be associated with a
# person's name, so each burger can be given
# to the right person.



# constants
BURGER_FILLINGS = ["Tomato", "Cheese", "Chicken", "Beef", "Onion", "Lettuce"]

# variables
all_orders = {}


def collect_order():
    
    # greet the person
    print("Hi! Welcome to Burger Builder :)")
    print("What would you like in your burger today?\n")
    
    # each burger is a list of fillings
    # so create a list to store their choices
    burger = []
    
    # list the filling options
    print("Our filling options are:")
    for filling_option in BURGER_FILLINGS:
        print(filling_option)
        
    # explain how to add a filling
    print("\nType the name of a filling to add it to your burger, or type 'done' to finish your order.")
    
    user_done = False
    
    # keep asking until they say they're done
    while user_done == False:
    
        # ask them to choose a filling
        filling_choice = input("\nWhat would you like to add?")
        
        # only add the filling if it is valid
        if filling_choice in BURGER_FILLINGS:
            burger.append(filling_choice)
            print("Great! So far your burger contains:")
            for filling in burger:
                print(filling)
        
        elif filling_choice == 'done':
            user_done = True
            print("Okay, so that's all for today.")
            
        else:
            print("Sorry, we don't have any " + filling_choice)
    
    
    # ask for a name
    person_name = input("\nAnd what name should I put that order under?")
    
    # save the order against the person's name
    all_orders[person_name] = burger
    
    # confirm the order with the person
    print("\nThanks " + person_name)
    print("Your burger will have:")
    for filling in burger:
        print(filling)

    
collect_order()



