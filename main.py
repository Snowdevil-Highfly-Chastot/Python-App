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
from kivy.properties import StringProperty, NumericProperty
from py.classMachine import Job

Builder.load_file("kv/ScreenManagement.kv")

class MainOverview(Screen):
    selectedMachine = StringProperty()
    
class MachineStatusPage(Screen):
    selectedMachine = MainOverview.selectedMachine
    
    Machine_Name = selectedMachine
    Part_Name = StringProperty("PartNameTest")
    Part_Desc = StringProperty("PartDescTest")
    Time_Per_Part = str(NumericProperty(100))
    Oal = NumericProperty(1.2)
    Cut_Off_Width = NumericProperty(.1)
    Bar_Length = NumericProperty(300)
    Bar_Parameter = NumericProperty(4.1)
    
    
        
    
class AddMachinePage(Screen):
    pass
class AddJobPage(Screen):
    
    Machine_Name = MainOverview.selectedMachine
    Part_Name = StringProperty()
    Part_Desc = StringProperty()
    Time_Per_Part = NumericProperty()
    Oal = NumericProperty()
    Cut_Off_Width = NumericProperty()
    Bar_Length = NumericProperty()
    Bar_Parameter = NumericProperty()
    
    def addNewJob():
        newJob = Job(Machine_Name, Part_Name, Part_Desc, Time_Per_Part, "", Oal, Cut_Off_Width, Bar_Length, Bar_Parameter, Active = "y")
        newJob.postJob()
        
    
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
        

        with root.canvas.before:
            Color(0, 1, 1, .6)  # colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MainApp().run()
