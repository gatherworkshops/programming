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

      You can specify the width as a number of characters.

      ```python
      entry = tkinter.Entry(window)
      entry.config(width=20)
      entry.grid()
      ```
      {: data-line="1,3" }


  

  - content: |

      ## Validating on Enter

      ```python
      entry = tkinter.Entry(window)
      entry.config(width=20)
      entry.bind("<Return>", validate_entry)
      entry.grid()

      def validate_entry():
          entry_text = entry.get()
          errors = []
          // do validation
      ```
      {:data-line="1-2,4"}


  - content: |
      
      ## Validating Input Length

      ```python
      def validate_text():
          entry_text = entry.get()
          error = None

          if(len(entry_text) < 3):
              error = "Length must be greater than 3 letters."
      ```

  - content: |

      ## Validating Text-Only

      ```python
      def validate_text():
          entry_text = entry.get()
          error = None 

          if len(entry_text) < 3:
              error = "Length must be greater than 3 letters"

          if entry_text.replace(" ", "").isalpha():
              error += "Sorry, special characters aren't allowed"
      ```

  - content: |

      ## Validating Positive Numbers

      ```python
      def validate_integer():
          entry_text = entry.get()
          error = None

          if !entry_text.isdigit():
              errors.append("Input must be positive numbers only")
      ```

  - content: |

      ## Validating any Number

      ```python
      def validate_integer():
          entry_text = entry.get()
          errors = [] 

          if !entry_text.isdigit():
              errors.append("Input must be positive numbers only")
      ```


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