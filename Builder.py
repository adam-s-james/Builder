import kivy
## kivy.require('1.0.6') # replace with your current kivy version ! (not by Adam)

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class Medicine:
    def __init__(self, name, strength, form, admin_time_1, admin_time_2, admin_time_3, admin_time_4, admin_time_5):
        self.name = name
        self.strength =strength
        self.form = form
        self.admin_time_1 = admin_time_1
        self.admin_time_2 = admin_time_2
        self.admin_time_3 = admin_time_3
        self.admin_time_4 = admin_time_4
        self.admin_time_5 = admin_time_5
        self.administered = False

    def administer_medicine(self):
        self.administered = True

        
class User:
        def __init__(self, name, surname):
            self.name = name
            self.surname = surname

            def welcome(self):
                print("")


class Alpha(Widget): #my root kivy widget, Mprime returns this widget
    def updateText(self): # seeupdates the original Label:button1 text to
        self.ids.label_1.text="Medicine added to your list!"

# Main app ==== kivy - kv file musy be named (lowercase!) after this minus any "App" if this is part of the app name
class Mprime(App):

    def build(self):
        return Alpha()

# ===============


if __name__ == '__main__':
    Mprime().run()