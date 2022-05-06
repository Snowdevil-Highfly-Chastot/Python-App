from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)
        
        def callback(self):
            print('The button <%s> is being pressed' % self.text)
            self.text = ("Pressed")
        
        #button describing
        btn1 = Button(
            text="Button 1",
            size_hint=(.90, .10),
            pos_hint={'center_x': .5, 'center_y': .8})
            
        btn2 = Button(
            text="Button 2",
            size_hint=(.90, .10),
            pos_hint={'center_x': .5, 'center_y': .7})

        # let's add a Widget to this layout
        self.add_widget(
            Button(
                text="Hello World",
                size_hint=(.90, .10),
                pos_hint={'center_x': .5, 'center_y': .9})
)
                
        self.add_widget(btn1)
        btn1.bind(on_press=callback)
        self.add_widget(btn2)
        btn2.bind(on_press=callback)


class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
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