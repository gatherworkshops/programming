---
layout: chapter
title: Skills Review
course: levelthree

slides:

  - title: title-page
    class: title-slide

    notes: |

      :)

    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/assets/images/gw_logo.png)

      # Skills Review
      _What we (should) already know_


##########


  - title: datatypes
    class: centered-slide

    notes: |

      There are a bunch of data types in Python, which you should already be familiar with.

      More data types do exist, but these are all the ones you should need.

    content: |

      ## Data Types

      string integer float boolean list dictionary


##########


  - title: typecasting
    class: centered-slide

    notes: |

      We can also convert between different data types. The most common conversion is turning a string into something more useful, like a number or a boolean.

      You most frequently need type conversion or "typecasting" when interpreting user input.

    content: |

      ## Type Casting

      string to integer
      string to boolean


##########


  - title: userinput
    class: centered-slide

    notes: |

      Receiving user input from the command line is the most simple way to have your user interact with your program.

      Whenever we capture user input, we store it in a variable.

      Captured user input is always in string (text) format unless we specifically convert it to something else.

    content: |

      ## User Input

      ```python
      user_input = input("What is your name?")
      ```

##########


  - title: listsanddicts
    class: centered-slide

    notes: |

      We can also group data together in a few different ways.

      For an ordered group of values, we can use a list.

      For an unordered group of values, accessible by name, we an use a dictionary.

    content: |

      ## Lists and Dictionaries

      ```python
      names = [
        "Aroha"
        "Billy",
        "Clare"
      ]
      ```

      ```python
      scores = {
        "Alistair": 30,
        "Beyonce": 70,
        "Clive": 50
      }
      ```


##########


  - title: loops
    class: centered-slide

    notes: |

      Loops let us run the same piece of code over and over until a condition is met.

      Some common conditions would be:

      - A counter has reached a given limit
      - Every item in a list has been processed
      - A boolean value is no longer true

    content: |

      ## Loops

      Do the same thing over...
      and over... and over...

##########

  - title: conditionals
    class: centered-slide

    notes: |

      Conditionals are more commonly known as "if statements", and can be used to only run a piece of code if a given condition evaluates to "true".

    content: |

      ## Conditionals

      if, elif, else


##########


  - title: challenge
    class: centered-slide
    content: |
      
      ![Burger]([[BASE_URL]]/media/images/icons/burger.svg){: height="200"}

      ## Challenge: <br>Debug the Burger Builder

      Open up `burgerbuilder.py` and make it work better:

      1. All unchanging values should be stored in constants.
      2. The app should apologise if it doesn't have a requested filling.
      3. The app should be able to collect as many orders as needed.


##########


  - title: summary
    class: centered-slide

    notes: |

      Great! Now the basics are covered, let's do some new stuff!

    content: |

      ![Thumbs Up!]([[BASE_URL]]/assets/images/thumbs-up.svg){: height="200"}

      ## Skills Review: Complete!

      Great, now it's time for the new stuff...

      [Take me to the next chapter!](gui.html)


---


[Double Burger by Arthur Shlain from the Noun Project](https://thenounproject.com/search/?q=burger&i=190703)