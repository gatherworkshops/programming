---
layout: default
bodyclass: chapter
title: Layouts
course: levelthree

slides:

  - title: title-page
    class: title-slide

    notes: |

      :)

    content: |

      # Layouts
      _Putting widgets in their place_


#########


  - title: geometrymanagers 
    class: centered-slide
    
    notes: |
      A geometry manager figures out where to put widgets within a window, based on instructions that you provide.

      There are three types of geometry manager available in Tk: pack, grid and place.

      We will only be covering the Grid Manager, as learning that one will allow you to achieve the majority of layouts.

    content: |

      ## Geometry Managers

      ![Pack, Grid, and Place Layouts](assets/images/geometry-managers.svg)


##########

  
  - title: gridlayout
    class: centered-slide 

    notes: |

      The Grid Manager allows you to create a grid using rows, columns and cells.

      There is no need to create a grid first - telling the widgets where to be placed creates the grid automatically.

    content: |

      ## Grid Layouts   

      Grid layouts are used most frequently,
      so we will focus on the Grid Manager 


##########


  - title: simplegrid
    class: centered-slide

    notes: |

      Let's start by making a simple grid.

      To create a simple grid we will have a traditional table layout with two columns and four rows. 

    content: |

      ## Simple Grid

      Open up `simplegrid.py` and add these two labels:

      ```python
      field_heading = tkinter.Label(window)
      field_heading.config(text="Field Name", font="Verdana 10 bold")
      field_heading.grid(row=0, column=0)

      value_heading = tkinter.Label(window)
      value_heading.config(text="Value", font="Verdana 10 bold")
      value_heading.grid(row=0, column=1)
      ```

      Your app should have two bold labels side by side
      {: .checkpoint }


##########


  - title: completethegrid
    class: centered-slide

    notes: |

      Add some more labels and some fields to make your app look like this.

    content: |

      ## Complete Your Grid

      ![Simple Grid Demo](assets/images/simple-grid-demo.svg)

      Add widgets so your app looks (sort of) like the example
      {: .checkpoint }


##########

  - title: resizing
    class: centered-slide

    notes: |

      Currently, our grid cells only grow to contain the widgets within them.

      To make our grid resize with our app window, we can configure columns to resize appropriately.

      A weight of `0` means "don't resize".

      All other numbers are calculated as a ratio, giving more space to the columns with bigger numbers.

      A column with a weight of 2 will grow twice as fast as a column with a weight of 1 as the user resizes the window.

    content: |

      ## Resizing

      We can configure columns to resize at different rates:

      ![Simple Grid Demo](assets/images/resizing.svg)

      ```python
      window.columnconfigure(0, weight=0)
      window.columnconfigure(1, weight=1)
      ```

      Your grid should grow to fit a resized window
      {: .checkpoint }


##########


  - title: stickiness
    class: centered-slide

    notes: |

      Within cells, we can make the widget "stick" to a particular side of the cell using the sticky property.

    content: |

      ## Stickiness

      Widgets are aligned within cells using compass points:

      ![Sticky Locations](assets/images/stickiness.svg){: height="400" }


##########


  - title: stickylabel
    class: centered-slide

    notes: |

      When we stick to more than one side, the widget will resize as the cell resizes.

    content: |

      ## Sticky Label

      Here's how you would stretch an entry field:

      ```python
      firstname_entry = tkinter.Entry(window)
      firstname_entry.grid(row=1, col=1, sticky="we")
      ```

      Your "First Name" entry should resize with the window
      {: .checkpoint }


##########


  - title: stickyform
    class: centered-slide

    notes: |

      Use the sticky setting to align all of the labels and entry boxes in your form.

    content: |

      ## Sticky Form

      Align your form widgets to look like this:

      ![Sticky Form](assets/images/sticky-form.svg){: height="300" }

      Your form should resize smartly, like in the picture
      {: .checkpoint }


##########


  - title: complexgrid
    class: centered-slide

    notes: |

      Grids can be as simple or as complex as you want them to be.

    content: |
      ## Complex Grid

      ![Complex Grid](assets/images/complex-grid.svg){: height="400" }

      Open up `membermanager.py`.

      Now we will use the same concept to create
      a more complex layout.




##########


  - title: divideintocells
    class: centered-slide

    notes: |

      The first step in creating a complex grid application is splitting it up into cells.

      To do this, draw a line between every widget and its neighbour both horizontally and vertically.

      Check that the top left of every widget aligns with the top left of a grid cell.

    content: |
      ## Divide into Cells

      ![Dividing Up a Complex Grid](assets/images/divide-into-cells.svg){: height="400" }

      Divide your layout into cells by drawing lines
      between neighbouring widgets.


##########


  - title: identifycontentcells
    class: centered-slide

    notes: |

      Next step is to identify which cells contain the top left corner of each widget.

      These cells will contain the widget initially, and then we will use extra settings to stretch the widgets across multiple cells.

    content: |
      ## Identify Content Cells

      ![Identifying Content Cells](assets/images/find-content-cells.svg){: height="400" }

      Highlight every cell which contains
      the top left corner of a widget.


##########


  - title: measurespans
    class: centered-slide

    notes: |

      The last piece of information we need for each widget is how many rows and columns it spans.

    content: |
      ## Find Spanning Cells

      ![Measuring Rowspan and Colspan](assets/images/find-spanning-cells.svg){: height="400" }

      Highlight row spans and column spans
      for any widgets that need it.


##########


  - title: applysettings
    class: centered-slide

    notes: |

      We can also choose to make a single cell span across multiple columns.

    content: |

      ## Apply Settings

      You can now use the information to arrange the widgets in the grid:

      ```python
      title_label = tkinter.Label(window)
      title_label.config(text="Super Duper Member Manager")
      title_label.grid(row=0, column=0, columnspan=4)
      ```
      {: data-line="1-2" }

      Apply the correct row, column and spans to all widgets
      {: .checkpoint }

##########


  - title: challenge
    class: centered-slide

    notes: |

      Reproduce this layout using the Grid Manager.

    content: |

      ## Challenge:<br>Happy Shopper

      ![Happy Shopper Challenge](assets/images/grid-challenge.svg){: height="400" }

      Create a new app called `happyshopper.py`
      and reproduce this grid layout.


##########


  - title: summary
    class: centered-slide

    notes: |

      Great! Now that's all sorted, let's get started!

    content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200" }

      ## Layouts: Complete!

      Cool, now we need to make it all actually work...
      [Take me to the next chapter!](events.html)


---


<section class="container content-panel" markdown="1">

## Geometry Managers Demo Page

[Tkinter Geometry Managers](http://userpages.umbc.edu/~dhood2/courses/cmsc433/spring2010/?section=Notes&topic=Python&notes=94)

All three types of geometry managers demonstrated on one page, with both code and screenshots of the resulting apps.

Highly recommended.

</section>



<section class="container content-panel" markdown="1">

## Grid Manager Reference

[The Tkinter Grid Geometry Manager](http://effbot.org/tkinterbook/grid.htm)

A focus on the grid manager with a few examples, and a settings reference at the bottom.

Worth a read when you have a few minutes.

</section>

