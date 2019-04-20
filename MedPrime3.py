import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout): #inheriting from Gridlayout
    def __init__(self, **kwargs): #kwargs means can take as may arguments as we want
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 4
        self.add_widget(Label(text="Medicine:"))
        self.medicine = TextInput(multiline=False) #declaring new textinput: medicine
        self.add_widget(self.medicine) #Adding medicine textinput widget to grid

        self.add_widget(Label(text="Strength:"))
        self.strength = TextInput(multiline=False)  # declaring new textinput: strength
        self.add_widget(self.strength)  # Adding strength textinput widget to grid

        self.add_widget(Label(text="Form:"))
        self.form = TextInput(multiline=False) #declaring new textinput: form
        self.add_widget(self.form) #Adding form textinput widget to grid


class MedPrime(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MedPrime().run()