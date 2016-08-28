
import kivy
kivy.require('1.9.1')

from kivy.app import App
from mainscreen import MainScreen

class MasterDetail(App):
    
    def build(self):
        self.title = "Master Detail Demo"
        return MainScreen()


if __name__ == '__main__':
    MasterDetail().run()