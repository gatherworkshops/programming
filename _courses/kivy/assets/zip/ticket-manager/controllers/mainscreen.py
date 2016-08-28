from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

class MainScreen(BoxLayout):

    Builder.load_file('templates/mainscreen.kv')
    

    label_wid = ObjectProperty()
    info = StringProperty()

    def __init__(self):
        super(MainScreen, self).__init__()
        


    def do_action(self):
        self.label_wid.text = 'After press'
        self.info = 'New info text'