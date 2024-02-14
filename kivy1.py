from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class layout1(GridLayout):
    """docstring for layout1"""
    def __init__(self, **kwargs):
        super(layout1, self).__init__(**kwargs)
        self.cols = 2


        self.add_widget(Label(text="FirstName: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="LastName: "))
        self.LastName = TextInput(multiline=False)
        self.add_widget(self.LastName)

        self.add_widget(Label(text="email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.button = Button(text="Submit", font_size=40)
        self.add_widget(self.button)


        
class kivy1App(App):
    def build(self):
        return layout1()
        # return Label(text="SSup guy", font_size=55)


if __name__ == '__main__':
    kivy1App().run()