
import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.config import Config
from controllers.mainscreen import MainScreen

class TicketManager(App):

    Config.update_config('config.ini', True)

    
    def build(self):
        self.title = "yippeeee!"
        return MainScreen()


if __name__ == '__main__':
    TicketManager().run()