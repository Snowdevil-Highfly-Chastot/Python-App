from py.config.mainImports import *
from kv.widgets import *
from kv.screens import *

class MainApp(App):

    def build(self):

        #Creates db folder to hold the database, if it doesn't already exist.
        Path("db").mkdir(parents=True, exist_ok=True)
        #Removes application exit from android back button press.
        Config.set('kivy', 'exit_on_escape', '0')
        #Creates root app and sets to a screen based Kivy application
        self.root = root = ScreenManager()
        #Binds the rectangle function below to the size of the window, to set the applications background
        root.bind(size=self._update_rect, pos=self._update_rect)
        #Creates all the screens from the classes above and adds them as widgets to the screenmanager
        screen1 = MainOverview(name='MainOverview')
        screen2 = MachineStatusPage(name='MachineStatusPage')
        screen3 = AddMachinePage(name='AddMachinePage')
        screen4 = AddJobPage(name='AddJobPage')
        screen5 = MainOverviewDelete(name='MainOverviewDelete')
        root.add_widget(screen1)
        root.add_widget(screen2)
        root.add_widget(screen3)
        root.add_widget(screen4)
        root.add_widget(screen5)

        #Creates the actual background rectangle and colors it
        with root.canvas.before:
            Color(*get_color_from_hex('2D3142'))  # colors range from 0-1 not 0-255 if not using hex
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    #Function to run and keep running while the app runs, automatically updates the size of the recangle to match the window size
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

#Runs the application
if __name__ == '__main__':
    MainApp().run()
