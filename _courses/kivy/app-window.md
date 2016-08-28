---
layout: default
title: Welcome
course: levelthree

slides:

  - content: |

      # App Window
      _Creating a window for your app_

  

  - content: |

      ## Create a file called `widgetdemo.py`

      ```python
      import kivy
      kivy.require('1.9.1')

      from kivy.app import App
      from kivy.uix.boxlayout import BoxLayout

      class WidgetDemo(App):

          def build(self):
              return BoxLayout()


      if __name__ == '__main__':
          WidgetDemo().run()
      ```

      When you run this app you should see a black window.
      {:.checkpoint}

    notes: |

      The most basic Kivy app is simply an app launcher Python file which displays a single Kivy widget, in this case a BoxLayout.

      A BoxLayout is just an empty box, which is why our app looks super boring so far!

      In the first two lines we import Kivy and specify the minimum version required to run the app.

      We then import `App` and `BoxLayout` from the Kivy library. We must always import `App` in our app launcher file. We are only importing `BoxLayout` because we are using it... for now.

      Our app is a class called `WidgetDemo` which extends `App`.

      Inside the class we define a `build` function which returns a BoxLayout. The `build` function and returning a widget is a structure specific to Kivy.

      At the end of the file is our Python app entry point, which you should be familiar with. It creates and runs an instance of our WidgetDemo class.





  - content: |

      ## Create a file called `mainscreen.kv`

      ```yaml
      #:kivy 1.0

      <MainScreen>

          Label:
              text: 'Woooo I'm alive!'
      ```

      This is a template file which displays a label.
      Don't panic, it won't work just yet!

    
    notes: |

      In Kivy apps, template files have the file extension `.kv` which stands for "Kivy".

      Template files don't automatically work on their own. We need to create a Python file to control them template, and attach the template to it.

      We'll look for deeply at the Kivy templating language soon.


    
  - content: |

      ## Create a file called `mainscreen.py`

      ```python
      from kivy.lang import Builder
      from kivy.uix.boxlayout import BoxLayout

      class MainScreen(BoxLayout):

          Builder.load_file('templates/mainscreen.kv')
      ```

      This is a controller file which loads a template.
      We can make our app launcher display this screen.


    notes: |

      None


  - content: |

      ## Load the MainScreen from your app launcher

      ```python
      import kivy
      kivy.require('1.9.1')

      from kivy.app import App
      from kivy.uix.boxlayout import BoxLayout # remove
      from mainscreen import MainScreen

      class WidgetDemo(App):

          def build(self):
              return BoxLayout() # change
              return MainScreen()


      if __name__ == '__main__':
          WidgetDemo().run()
      ```
      {: data-line-delete="5" data-line-add="6"}

      When you run the app you should see a label.
      {:.checkpoint}





  - content: |

      ## Customise the App Title

      ticketmanager.py

      ```python
      class TicketManager(App):

        def build(self):
            self.title = "Wheeee" #added
            return MainScreen()
      ```

      Your app window should now have a custom name in the title bar.
      {:.checkpoint}



---