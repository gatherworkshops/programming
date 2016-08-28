---
layout: default
title: Interactive Buttons

slides:

  - content: |

      # Interactive Buttons
      _Interacting with user clicks_

    notes: |

      To create a GUI or Graphical User Interface, we can use a set of ready-made widgets which come with Python.

      These widgets can be combined in any layout to create a basic app.
    

  - content: |

      ## Create a new app called `button-demo.py`

      ```python
      import tkinter
      window = tkinter.Tk()

      window.title("Button Demo")
      window.geometry("300x300")

      window.mainloop()
      ```

      You should have an empty app called "Button Demo".
      {:.checkpoint}



#########


  - content: |
      ## Creating a Button
      
      Create a button and add it to your window:

      ```python
      window.title("Button Demo")
      window.geometry("300x300")

      button = tkinter.Button(window)
      button.config(text="Click Me!")
      button.grid()

      window.mainloop()
      ```
      {: data-line="1-2, 8" }

      Your window should now contain a button
      {: .checkpoint }
    
    notes: |

      We can also create buttons with ease.


  - content: |

      ## Handling a Click

      We use `bind` to link a button click to a function.

      ```python
      import tkinter

      def say_hello(event):
          print("Why hello there!")
 
      window = tkinter.Tk()

      window.title("Button Demo")
      window.geometry("300x300")

      button = tkinter.Button(window)
      button.config(text="Click Me!")
      button.bind("<Button>", say_hello)
      button.grid()

      window.mainloop()
      ```
      {: data-line="1, 6-12, 14-16"}

      The function must be defined *before* it is bound to a button.


      Your button should print "Why hello there!" in the console.
      {:.checkpoint}



  - content: |

      ## Separating Design and Function

      To keep our app tidy, we should group functionality
      and the interface design under clear headings.

      ```python
      import tkinter

      # APP FUNCTIONALITY ***************

      def say_hello(event):
          print("Why hello there!")

      # APP INTERFACE *******************

      window = tkinter.Tk()

      window.title("Button Demo")
      window.geometry("300x300")

      button = tkinter.Button(window)
      button.config(text="Click Me!")
      button.bind("<Button>", say_hello)
      button.grid()

      window.mainloop()
      ```

      Keeping our code tidy makes it easier to make changes.




  - content: |

      ## Updating the UI from a Click Handler

      Import the `random` library:

      ```python
      import random
      ```

      Under **App Functionality** add a function to generate a number:

      ```python
      def generate_random_number(event):
          number = random.randint(1, 10)
          random_label.config(text=number)
      ```

      Under **App Interface** add a label and a button:
      
      ```python
      random_label = tkinter.Label(window)
      random_label.config(text="No number yet :(")
      random_label.grid()

      random_button = tkinter.Button(window)
      random_button.config(text="Generate Random Number")
      random_button.bind("<Button>", generate_random_number)
      random_button.grid()
      ```

      Clicking the button should display a random number.
      {:.checkpoint}
      



  
#  - content: |
#
#      ## Creating an Icon Button
#
#      Add a new button which displays only an icon.
#
#      ```python
#      icon_button = tkinter.Button(window)
#      icon_button.config(image='icons/settings.png')
#      icon_button.grid()
#      ```
#      
#      You should see a button with a settings icon.
#      {:.checkpoint}



#  - content: |
#
#      ## Creating a Labeled Icon Button
#
#      Add a new button which has both a label and an icon.
#
#      ```python
#      icon_label_button = tkinter.Button(window)
#      icon_label_button.config(text='Settings')
#      icon_label_button.config(image='icons/settings.png')
#      icon_label_button.config(compound=LEFT)
#      icon_label_button.grid()
#      ```
#
#      You should see a button with an icon to the left of a label.
#      {:.checkpoint}


  - content: |

      ## Disabling a Button

      Add a new button to your app.
      

      ```python
      disabled_button = tkinter.Button(window)
      disabled_button.config(text="Unclickable")
      disabled_button.config(state=tkinter.DISABLED)
      disabled_button.grid()
      ```

      Disable a button by configuring its state.

      Your app should now include a disabled button.
      {:.checkpoint}

  - content: |

      ## Challenge: Danger Zone

      Create an app called `danger-zone.py` to display a danger level
      which the user can update to be low, medium or high.

      The button for the current selection should be disabled.


  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200" }

      ## Interactive Buttons: Complete!

      Groovy, but what about capturing user data...
      [Take me to the next chapter!](entry.html)

    notes: |

      Great! Now that's all sorted, let's get started!

    
      
    
    
    

---