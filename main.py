from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.colorpicker import ColorPicker
from py.fileImport import readMachine
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.properties import StringProperty
<<<<<<< HEAD

Builder.load_file("kv/ScreenManagement.kv")


class MainOverview(Screen):
    button_1 = ''
class MachineStatusPage(Screen):
    selectedMachine = StringProperty()
    def getInfo(self, selectedMachine):
        button1 = MainOverview.button_1.text
        self.selectedMachine.append(button1)
        return selectedMachine
=======

Builder.load_file("kv/screenMaster.kv")

class MainOverview(Screen):
    selectedMachine = StringProperty("")
class MachineStatusPage(Screen):
    selectedMachine = StringProperty("yo")
>>>>>>> 9704b6d (Working on dynamic labeling)
class AddMachinePage(Screen):
    pass
class AddJobPage(Screen):
    pass

class Variables():
    selectedMachine = StringProperty()
    def getInfo(self, selectedMachine):
        button1 = MainOverview.button_1.text
        self.selectedMachine.append(button1)
        return selectedMachine

class MainApp(App):   

    def build(self):
        
        self.root = root = ScreenManager()
        root.bind(size=self._update_rect, pos=self._update_rect)
        screen1 = MainOverview(name='MainOverview')
        screen2 = MachineStatusPage(name='MachineStatusPage')
        screen3 = AddMachinePage(name='AddMachinePage')
        screen4 = AddJobPage(name='AddJobPage')
        root.add_widget(screen1)
        root.add_widget(screen2)
        root.add_widget(screen3)
        root.add_widget(screen4)
        
        #selectedMachine = StringProperty('test')
        

        with root.canvas.before:
            Color(0, 1, 1, .6)  # colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MainApp().run()