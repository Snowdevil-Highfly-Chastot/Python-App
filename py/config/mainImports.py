import time
from py.classes import Job, Machine
from py.mainLibrary import readMachines
from py.sqlite import readMachine
from kivy.app import App, runTouchApp
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.config import Config
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from pathlib import Path