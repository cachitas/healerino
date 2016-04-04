"""
Healerino
=========

"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout


class Game(BoxLayout):
    pass


class Healerino(App):

    def build(self):
        return Game()


if __name__ == '__main__':
    Healerino().run()
