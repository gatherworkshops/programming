from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView

class MainScreen(BoxLayout):

    Builder.load_file('mainscreen.kv')

    contact_data = ListProperty([])

    def __init__(self):
        super(MainScreen, self).__init__()

        self.contact_data.append({
            'name': 'Person One'
        })
        


    def do_action(self):
        self.label_wid.text = 'After press'
        self.info = 'New info text'