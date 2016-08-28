---
layout: default
bodyclass: chapter
title: The App Window
course: levelthree

slides:


  - content: |

      # The App Window
      _Creating a visual container for your application_



  - content: |
      
      ## Creating a Window

      Create a file called `window-demo.py` with the following code:

      ```python
      import tkinter
      window = tkinter.Tk()
      window.mainloop()
      ```

      You should see a window when you run your app.
      {:.checkpoint}

    notes: |

      To get started creating our app, the first thing we need to do is import tkinter and create an app window.

      Importing tkinter allows us to create windows and also the widgets that we explore later.

      Calling the `mainloop` function starts your app running, and should always be done after setup.




  - content: |
      ## Customising the Title

      Customise your app's name:

      ```python
      import tkinter
      window = tkinter.Tk()

      window.title("Window Demo")

      window.mainloop()
      ```
      {: data-line="1-2, 6" }

      Your window should now have a customised title bar.
      {:.checkpoint}
    
    notes: |

      The default window has no title.

      We can customise our window a little using methods provided by tkinter.



  - content: |
      ## Customising the Window Size

      Customise the window size:

      ```python
      import tkinter
      window = tkinter.Tk()

      window.title("Widget Demo")
      window.geometry("800x600")

      window.mainloop()
      ```
      {: data-line="1-4, 7" }

      Your window should now be bigger.
      {:.checkpoint}
    
    notes: |

      The default window is 200 pixels square when there is nothing in it.

      Once widgets are added, the window automatically sizes itself to fit its content.


## TODO: Customise the window location


## TODO: Center the window on the screen




  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## The App Window: Complete!

      Great, now let's look at some widgets...

      [Take me to the next chapter!](label.html)

    notes: |

      Great! That's the basics out of the way, now let's move on to layouts.

    


    
---