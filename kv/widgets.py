from py.config.mainImports import *

#The ButtonBoxLayout is used to encase the machine buttons on the Overview,
#and have clicking attributes
class ButtonBoxLayout(ButtonBehavior, BoxLayout):

    background_color = ListProperty((get_color_from_hex('4F5D75')))

    def on_state(self, widget, value):
        if value == 'down':
            self.background_color = (get_color_from_hex('E0F1FF'))
        else:
            self.background_color = (get_color_from_hex('4F5D75'))

#The ToggleBoxLayout is used in the Machine Delete screen.
#It is the same as ButtonBoxLayout except has toggle functionality
#to allow multiple machine selection for deleting.
class ToggleBoxLayout(ToggleButtonBehavior, BoxLayout):

    background_color = ListProperty((get_color_from_hex('4F5D75')))

    def on_state(self, widget, value):
        if value == 'down':
            self.background_color = (get_color_from_hex('E0F1FF'))
        else:
            self.background_color = (get_color_from_hex('4F5D75'))

#UiButton class widget is used in all of the single text buttons throughout
#the application
class UiButton(ButtonBehavior, Label):

    background_color = ListProperty((get_color_from_hex('4F5D75')))

    def on_state(self, widget, value):
        if value == 'down':
            self.background_color = (get_color_from_hex('E0F1FF'))
        else:
            self.background_color = (get_color_from_hex('4F5D75'))