---
layout: default
title: jQuery Basics
slides:


##########

  
  - title: title-page
    class: title-slide

    notes: |

      :)

    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/theme/assets/images/gw_logo.png)

      # jQuery Basics
      _Using jQuery on top of HTML and CSS_


  - title: languages
    class: centered-slide

    notes: |
      Websites are made of many languages, but your most basic web page, what you see in your browser, is made up of three programming languages.

      That's three different types of code, each with their own rules.

      They all work together to display what you see on the screen.

    content: |

      ## A web page is made of three main languages

      ![Venn diagram of HTML, CSS and JS all overlapping](assets/images/html-css-js.png)


##########


  - title: html
    class: centered-slide

    notes: |
      HTML is used to define the content of a web page: the words, the pictures, the links.

      It does not define any sizes, colours or layout.

      HTML stand for HyperText Markup Language.

      This is a picture of what Google looks like when you see only the HTML - no CSS or Javascript.

    content: |

      ## **HTML** is the markup language

      ![Screenshot of Google with only HTML enabled](assets/images/google-html.png)


##########

  
  - title: css
    class: centered-slide

    notes: |
      CSS is used to define the appearance of a web page: the colours, the sizes, the layout.

      It can be thought of as the design language.

      It tells our web browser how to display the HTML.

      CSS stands for Cascading Style Sheets.

      This is a picture of what Google looks like when you combine the HTML and CSS.

    content: |

      ### **CSS** is the design language

      ![Screenshot of Google with both HTML and CSS enabled](assets/images/google-css.png)


##########


  - title: javascript
    class: centered-slide

    notes: |
      JavaScript is used to define any interactivity on a web page: dropdowns, popups, anything that changes after the page is first loaded.

      It can be thought of as the interaction language.

      JavaScript is often known as JS for short, and is actually quite different from Java, which is another programming laguage with a similar name. Tricky!

      This is a picture of what Google looks like when you see all the HTML, CSS and JS working together.

    content: |

      ## **JavaScript** is the programming language

      ![Screenshot of Google with all of HTML, CSS, JS enabled](assets/images/google-javascript.png)

      

  ##########


  - title: getelements
    class: centered-slide

    notes: |

      We can use jQuery to find and capture elements on a page.

      To get an element or group of elements, we can use an ID, a class,
      or the type of element.

    content: |

      ## Getting Elements in jQuery

      We find elements using the same selectors as in CSS:
      
      - **Get one by id**
        `$('#logo')`
      - **Get many by class**
        `$('.photo')`
      - **Get all by tag**
        `$('img');`
      {:.flex-list}

      Only difference is we do it in brackets, with a dollar sign.


  ##########


  - title: changingelements
    class: centered-slide

    notes: |

      One we've got an element, we can do stuff to it:

    content: |

      ## Changing Elements

      Add or remove a class to change how it looks:
      
      ```javascript
      var header = $('#pageHeader');
      header.addClass('fancyBorder');
      header.removeClass('plainBorder');
      ```

      Change its size and position:

      ```javascript
      var allPhotos = $('.photo');
      allPhotos.width(100);
      allPhotos.left(300);
      ```

      Fade in or fade out:

      ```javascript
      var allImages = $('img');
      allImages.fadeIn();
      allImages.fadeOut();
      ```


  ##########


  - title: jquerywithunicorns
    class: centered-slide

    notes: |

      Open this practice in codepen.

    content: |

      ![Unicorn](assets/images/unicorn.svg){: height="300" }

      ## jQuery Basics with Unicorns

      <a href="http://codepen.io/gatherworkshops/pen/merJYM?editors=001" target="_blank">Click here to start</a>


  ##########


  - title: unicornclasses
    class: centered-slide

    notes: |

      Open this practice in codepen.

    content: |

      ## Make January Golden

      In your JavaScript panel, add the class "gold" to January:

      ```javascript
      var january = $('#january');
      january.addClass('gold');
      ```

      **Challenge:**

      - February should be orange
      - March should be pink
      - April should be blue
      - The others can be any colour


  ##########


  - title: unicornsizes
    class: centered-slide

    notes: |

      Change the sizes of specific unicorns using their names.

      The CSS says that every `unicorn` should have a height of 50%.

    content: |

      ## Make the August Unicorn Smaller

      In your JavaScript panel:

      ```javascript
      var august = $('#august .unicorn');
      august.height('40%');
      ```

      **Challenge:**

      - May should be the same height as August
      - March should be 70% of the height of her box
      

  ##########


  - title: events
    class: centered-slide

    notes: |

      Sometimes we dont want to do things automatically as soon
      as the page loads.

      Sometimes we want to do something after a certain amount
      of time, or when something happens like a click or a keyboard
      button being pressed.

    content: |

      ## Flying Pegasus Ponies

      Create a function containing the code you want to run:

      ```javascript
      function fly() {
        var unicorn = $(this);
        unicorn.animate({'margin-bottom':'+=15'}, 1000);
        unicorn.animate({'margin-bottom':'-=15'}, 1000, fly);
      }
      ```

      Tell the selected objects when to run the function:

      ```javascript
      var pegasusPonies = $('.pegasus');
      pegasusPonies.click(fly);
      ```

      Pegasus ponies should now fly when clicked.
      {:.checkpoint}


  ##########


  - title: unicornevents
    class: centered-slide

    notes: |
      :)

    content: |

      ## June's Disappearing Trick

      Create the `turnInvisible` function:

      ```javascript
      function turnInvisible() {
      var clickedUnicorn = $(this);
      clickedUnicorn.fadeOut();
      }
      ```

      Run the function when June is clicked:

      ```javascript
      var june = $('#june .unicorn');
      june.click( turnInvisible );
      ```

      June should now disappear when clicked.
      {:.checkpoint}



  ##########


  - title: jumpingunicorns
    class: centered-slide

    notes: |
      :)

    content: |

      ## Jumping Jacks

      Here's a function to make a unicorn jump:

      ```javascript
      function jump() {
        var unicorn = $(this);
        unicorn.animate({'margin-bottom': '+=20'}, 300);
        unicorn.animate({'margin-bottom': '-=20'}, 300);
      }
      ```

      **Challenge:**
      Make one of the unicorns jump when the `mouseover` event happens.


  ##########


  - title: summary
    class: centered-slide

    notes: |

      Great! Now that we know the basics, let's get started on our own projects.

    content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200" }

      ## jQuery Basics: Complete!

      Great, now it's time to build our own...

      [Take me to the next chapter!](lightbox.html)





---
