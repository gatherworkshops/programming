---
layout: default
title: Capturing Text Input

slides:

  - content: |
      
      # Capturing Text Input
      _Using the Entry widget to capture text_
  

  - content: |

      ## Create a new app called `entry-demo.py`

      ```python
      import tkinter

      window = tkinter.Tk()
      window.title("Entry Demo")
      window.geometry("300x300")

      window.mainloop()
      ```

      You should have an empty app called "Entry Demo".
      {:.checkpoint}





  - content: |
      ## Creating an Entry

      Add a text entry box to your app.

      ```python
      import tkinter

      window = tkinter.Tk()
      window.title("Entry Demo")
      window.geometry("300x300")

      entry = tkinter.Entry(window)
      entry.grid()

      window.mainloop()
      ```
      {: data-line="1-5, 10" }

      Your window should now contain a text entry area.
      {: .checkpoint }

    notes: |

      Creating text inputs can be done using the Entry widget.



    
  - content: |

      ## Setting the Entry Size

      Specify the width of the entry box as a number of characters.

      ```python
      entry = tkinter.Entry(window)
      entry.config(width=20)
      entry.grid()
      ```
      {: data-line="1,3" }


  

  - content: |

      ## Input Validation

      ```python
      entry = tkinter.Entry(window)
      entry.config(width=20)
      entry.config(validatecommand=entry_is_valid)
      entry.config(validate=focusout)
      entry.grid()

      def entry_is_valid():
          return false

      ```


  - content: |

      ## Running a Function on Enter

  - content: |

      ## Setting the Entry Colours

      - foregoround
      - background
      - borders

  - content: |

      ## Running a Function on Focus Out

  - content: |

      ## Limiting the Input Length

      By running a function each time the user types.

  - content: |

      ## Text Validation

      - invalid
      - boundary
      - expected

  - content: |

      ## Numeric Validation

      - invalid
      - boundary
      - expected


  - content: |

      ## Challenge: 


  

    



---