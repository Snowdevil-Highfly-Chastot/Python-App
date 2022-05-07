from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from py.fileImport import readMachine


class StartWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(StartWidget, self).__init__(**kwargs)

        #Widget functions
        def readMachineFromDb ():
            machine = self.machineNameI.text
            readMachine(machine)
        
        #widget describing
        headerL = Label(
            text = 'Machine Test Calculations',
            font_size = (28),
            size_hint=(.90, .10),
            pos_hint={'center_x': .5, 'center_y': .9})

        machineNameL = Label(
            text = 'Enter Machine Name: ',
            font_size = (18),
            size_hint=(.45, .05),
            pos_hint={'center_x': .3, 'center_y': .8})

        self.machineNameI = TextInput(
            text = '',
            multiline=False,
            size_hint = (.45, .05),
            pos_hint={'center_x': .7, 'center_y': .8})

        btn1 = Button(
            text="Button 1",
            size_hint=(.90, .10),
            pos_hint={'center_x': .5, 'center_y': .7})
            
        btn2 = Button(
            text="Button 2",
            size_hint=(.90, .10),
            pos_hint={'center_x': .5, 'center_y': .6})

        # Adding Widgets to this layout
        self.add_widget(headerL)

        self.add_widget(machineNameL)
        self.add_widget(self.machineNameI)

        self.submit = (btn1)
        self.submit.bind(on_press = lambda x:readMachineFromDb())
        self.add_widget(self.submit)





class MainApp(App):

    def build(self):
        self.root = root = StartWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0, 1, 1, .6)  # colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MainApp().run()