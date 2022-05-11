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



class OuterGridLayout(FloatLayout):
    pass

Builder.load_file("kv/machineStatusPage.kv")
class MainApp(App):

    def build(self):
        self.root = root = OuterGridLayout()
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