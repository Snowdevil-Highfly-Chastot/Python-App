from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from py.fileImport import readMachine
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.properties import StringProperty
from py.classMachine import Job

Builder.load_file("kv/ScreenManagement.kv")

class MainOverview(Screen):
    selectedMachine = StringProperty()
    
class MachineStatusPage(Screen):

    selectedMachine = MainOverview.selectedMachine
    Machine_Name = selectedMachine
    
    Part_Name = StringProperty()
    Part_Desc = StringProperty()
    Parts_Needed = StringProperty()
    Time_Per_Part = StringProperty()
    

    Oal = StringProperty()
    Cut_Off_Width = StringProperty()
    Bar_Length = StringProperty()
    Bar_Parameter = StringProperty()
    
    Completion_Time = StringProperty()
    Time_Left = StringProperty()
    

    def getCurrentJob (self):

        currentJob = Job(self.Machine_Name)
        
        try:
            self.Part_Name = str(currentJob.grabJob(0))
            self.Part_Desc = str(currentJob.grabJob(1))
            self.Parts_Needed = str(currentJob.grabJob(4))
            self.Time_Per_Part = str(currentJob.grabJob(3))
            self.CompletionTime = str(currentJob.grabJob(5))
            
            self.Oal = currentJob.grabJob(6)
            self.Cut_Off_Width = currentJob.grabJob(7)
            self.Bar_Length = currentJob.grabJob(8)
            self.Bar_Parameter = currentJob.grabJob(9)
        except:
            self.Part_Name = "None"
            self.Part_Desc = "None"
            self.Time_Per_Part = "None"
            self.Parts_Needed = "None"
            
            self.Oal = "0"
            self.Cut_Off_Width = "0"
            self.Bar_Length = "0"
            self.Bar_Parameter = "0"
            
        updatedCurrentJob = Job(self.Machine_Name, " ", " ", self.Time_Per_Part, self.Parts_Needed)
        try:
            self.Time_Left = str(updatedCurrentJob.jobFinished())
        except:
            self.Time_Left = "None"
               
class AddMachinePage(Screen):
    pass
class AddJobPage(Screen):
    
    selectedMachine = MainOverview.selectedMachine
    
    Machine_Name = selectedMachine
    Part_Name = StringProperty()
    Part_Desc = StringProperty()
    Parts_Needed = StringProperty()
    Time_Per_Part = StringProperty()
    Oal = StringProperty()
    Cut_Off_Width = StringProperty()
    Bar_Length = StringProperty()
    Bar_Parameter = StringProperty()
    
    def addNewJob(self):
        newJob = Job(self.Machine_Name, self.Part_Name, self.Part_Desc, self.Parts_Needed, self.Time_Per_Part, "", self.Oal, self.Cut_Off_Width, self.Bar_Length, self.Bar_Parameter)
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
