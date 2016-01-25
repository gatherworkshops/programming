---
layout: chapter
bodyclass: chapter
title: User Interaction
course: levelthree

slides:

  - title: title-page
    class: title-slide

    notes: |

      :)

    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/assets/images/gw_logo.png)

      # User Interaction
      _Reacting to interface events_


##########


  - title: pythonevents
    notes: |

      Events are a common concept across languages, Python included.

      In programming, an event is something which happens in your app which you have the choice of programming your app to react to.

    content: |

      ## Python Events

      An "event" in Python is when something 
      happens that our app can react to.


##########


  - title: widgetevents
    notes: |

      The widgets available from the Tkinter library have a whole bunch of events programmed into them.

      We can tell our app to look out for those events, and to run specific code when they occur.

    content: |
      
      ## Widget Events

      Tkinter Widgets trigger different types of events
      when a user interacts with the app.


##########


  - title: eventtypes
    
    notes: |

      There are many types of events, but the ones we usually pay attention to are mouse events, keyboard events, and change events.

      These three types of events cover most of the user interactions that we care about.

    content: |

      ## Event Types

      The most common types of events are:

      - ![A Computer Mouse]([[BASE_URL]]/media/images/icons/mouse.svg){: height="150"}
        **Mouse Events**
        click, move, hover
      - ![Gaming Keys]([[BASE_URL]]/media/images/icons/gaming-keys.svg){: height="150"}
        **Keyboard Events**
        key down, key up
      - ![Resizing A Window]([[BASE_URL]]/media/images/icons/resize.svg){: height="150"}
        **Change Events**
        resize, select, focus
      {: .flex-list}


##########


  - title: thingsweneed
    
    notes: |

      When we want to react to an event, we need three things:

      1. Which widget will trigger it
      2. The exact name of the event
      3. A function to run when the event happens
      
      With this information, we can "bind" a function to the event.

      The function should contain code you only want to run when the event occurs.

    content: |

      ## Things We Need

      To react to an event we need three things:

      - **A Widget**<br>
        Which widget will trigger the event?
      - **The Event Name**<br>
        Which event are we expecting?
      - **A Function**<br>
        What code do we want to run in response?
      {: .flex-list}


##########

  - title: bindingcode
    
    notes: |

      Once we know which widget, which event, and which function, then we can write the code to tie them all together.

    content: |

      ## Event Binding

      We use the `bind` function to link all the parts together:

      ```python
      import tkinter
      window = tkinter.Tk()

      def say_hello(event):
          print("Why hello there!")

      mystery_button = tkinter.Button(window)
      mystery_button.config(text="Click Me")
      mystery_button.bind("<Button>", say_hello)
      mystery_button.grid()

      window.mainloop()
      ```
      {: data-line="1-2, 7-8, 10-12"}

      This is just an example - we'll do a demo next!


##########

  - title: eventsdemo
    
    notes: |

      Open up eventsdemo.py

    content: |

      ## Events Demo

      Open up `eventsdemo.py`
      so we can add some event handling to it.

 
##########

  - title: clickevent
   
    notes: |

      Add a click event using `<Button>`  

    content: |

      ## Click Events

      Add a click event binding to the `hello_button`:

      ```python
      hello_button = tkinter.Button(window)
      hello_button.config(text="Click Me")
      hello_button.bind("<Button>", say_hello)
      hello_button.grid()
      ```   
      {: data-line="1-2, 4" }

      Clicking the button should print "Hello!" in the console.
      {: .checkpoint}


##########

  - title: moreclickevents
    
    notes: |
      Make all the other buttons work, too.

    content: |

      ## More Click Events

      Make the other buttons work, too:

      - **Add Random Fruit**
      - **Delete Fruit**
      - **Generate Recipe**


##########


  - title: keyboardevents

    notes: |
      Make it so that pressing Enter while in the name input does the same thing as clicking Say Hello

    content: |

      ## Keyboard Events

      Bind the **name entry** box to the `<Return>` event,
      so that pressing "enter" does the same as clicking the button.


##########


  - title: challenge
  
    notes: |

      Add event bindings to the app. 

    content: |
      ## Challenge: Stuff To Do

      Complete `todo.py` with events and functionality
      so that it is a working To-Do app.


##########


  - title: summary
    class: centered-slide

    notes: |

      Great! Now that's all sorted, let's get started!

    content: |

      ![Thumbs Up!]([[BASE_URL]]/assets/images/thumbs-up.svg){: height="200" }

      ## User Interaction: Complete!

      Groovy, but what about more complex data...
      [Take me to the next chapter!](data.html)


---


<section class="container content-panel" markdown="1">

## Widget Events

### Mouse Buttons

- **`<Button>`**<br>
  Mouse click, any button
- **`<Button-1>`**<br>
  Mouse left-click
- **`<Button-2>`**<br>
  Mouse middle-click
- **`<Button-3>`**<br>
  Mouse right-click
- **`<Button-4>`**<br>
  Mouse scroll-up
- **`<Button-5>`**<br>
  Mouse scroll-down

### Mouse Movement




</section>

[Mouse by Olivier Guin from the Noun Project](https://thenounproject.com/search/?q=mouse&i=5534)

[Gaming Keys by Daniel Sikorski from the Noun Project](https://thenounproject.com/search/?q=single+keyboard+key&i=62295)

[Resize by Mister Pixel from the Noun Project](https://thenounproject.com/search/?q=resize&i=36733)