from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.lang import Builder


class StartWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(StartWidget, self).__init__(**kwargs)
        
        def callback(self):
            print('The button %s is being pressed' % self.text)
            self.text = ("Pressed")
        def writeback(self):
            print('The button %s is not being pressed anymore' % self.text)
            self.text = ('Button %s' % self.text)
        def on_enter(instance):
            print('User pressed enter in', instance)
        
        #widget describing
        header = Label(
            text = 'Machine Test Calculations',
            font_size = (28),
            size_hint=(.90, .10),
            pos_hint={'center_x': .5, 'center_y': .9})

        btn1 = Button(
            text="Button 1",
            size_hint=(.90, .10),
            pos_hint={'center_x': .5, 'center_y': .7})
            
        btn2 = Button(
            text="Button 2",
            size_hint=(.90, .10),
            pos_hint={'center_x': .5, 'center_y': .6})

        txtInput1 = TextInput(
            text='Hello world',
            multiline=False,
            size_hint = (.90, .10),
            pos_hint={'center_x': .5, 'center_y': .8})

        # Adding Widgets to this layout
        self.add_widget(header)

        self.add_widget(txtInput1)
        txtInput1.bind(on_text_validate=on_enter)

        self.add_widget(btn1)
        btn1.bind(on_press=callback)
        btn1.bind(on_release=writeback)

        self.add_widget(btn2)
        btn2.bind(on_press=callback)
        btn2.bind(on_release=writeback)


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