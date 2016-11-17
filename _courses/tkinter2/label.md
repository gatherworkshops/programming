---
layout: default
title: Text Labels

slides:

  - content: |

      # Text Labels
      _Displaying text in your app_

    notes: |

      To create a GUI or Graphical User Interface, we can use a set of ready-made widgets which come with Python.

      These widgets can be combined in any layout to create a basic app.




  - content: |

      ## Create a new app called `label-demo.py`

      ```python
      import tkinter
      window = tkinter.Tk()

      window.title("Label Demo")
      window.geometry("300x300")

      window.mainloop()
      ```

      You should have an empty app called "Label Demo".
      {:.checkpoint}
    



  - content: |
      ## Creating a Label

      Create a label and add it to your window:

      ```python
      window.title("Label Demo")
      window.geometry("300x300")

      label = tkinter.Label(window)
      label.config(text="Hello")
      label.grid()

      window.mainloop()
      ```
      {: data-line="1-2, 8" }

      Your window should now contain a label "Hello"
      {:.checkpoint}

    notes: |

      Let's explore some widgets available to us, starting with a simple label.    


  
  - content: |

      ## Setting the Font

      ```python
      label = tkinter.Label(window)
      label.config(text="Hello")
      label.config(font=("ComicSans"))
      label.grid()
      ```
      {: data-line="1-2, 4" }

      Your text should now be in Comic Sans.
      {:.checkpoint}

  - content: |

      ## Setting the Font and Size

      ```python
      label = tkinter.Label(window)
      label.config(text="Hello")
      label.config(font=("ComicSans", 22))
      label.grid()
      ```
      {: data-line="1-2, 4" }

      Your text should now be in Comic Sans and size 22.
      {:.checkpoint}
  

  - content: |

      ## Setting Bold and Italics

      ```python
      label = tkinter.Label(window)
      label.config(text="Hello")
      label.config(font=("ComicSans", 22, "bold", "italic"))
      label.grid()
      ```
      {: data-line="1-2, 4" }

      Your text should now be bold and italic.
      {:.checkpoint}


  - content: |

      ## Changing the Text Colour
      

      ```python
      label = tkinter.Label(window)
      label.config(text="Hello")
      label.config(font=("ComicSans", 22, "bold", "italic"))
      label.config(foreground="red")
      label.grid()
      ```
      {: data-line="1-3, 5" }

      To change the text colour, use the `foreground` property.
      You can use colour names or hex codes to set the colour.

      Your label text should now be red.
      {:.checkpoint}

  - content: |

      ## Displaying Multi-Line Text

      Create a new label component called `multiline_label`:

      ```python
      ...
      label.config(foreground="red")
      label.grid()

      long_label = tkinter.Label(window)
      long_label.config(text="Really long text that goes over more than one line to demonstrate how we do multi-line text in a label.")
      long_label.config(wraplength=200)
      long_label.grid()

      window.mainloop()
      ```
      {: data-line="1-3, 10" }

      Use the `wraplength` property to set the text width in pixels.

      Your text should wrap at 200px wide.
      {:.checkpoint}



  - content: |

      ## Aligning Label Text

      ```python
      long_label = tkinter.Label(window)
      long_label.config(text="Really long text that goes over more than one line to demonstrate how we do multi-line text in a label.")
      long_label.config(wraplength=200)
      long_label.config(justify="left")
      long_label.grid()
      ```
      {: data-line="1-3, 5-6"}

      Alignment options are `left`, `right`, and `center`.

      Your multi-line text should now be left-aligned.
      {:.checkpoint}


  - content: |

      ## Padding Labels

      Padding can be added either horizontally (`padx`) or vertically (`pady`):

      ```python
      long_label = tkinter.Label(window)
      long_label.config(text="Really long text that goes over more than one line to demonstrate how we do multi-line text in a label.")
      long_label.config(wraplength=200)
      long_label.config(justify="left")
      long_label.config(padx=20, pady=10)
      long_label.grid()
      ```
      {: data-line="1-4, 6"}

      Your text should now have extra spacing on all sides.
      {:.checkpoint}



  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Text Labels: Complete!

      Great, now let's make some buttons...

      [Take me to the next chapter!](button.html)

    notes: |

      Great! That's the basics out of the way, now let's move on to layouts.

    




---