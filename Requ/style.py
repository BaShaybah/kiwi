from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty,ColorProperty, NumericProperty 
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation 
from kivy.utils import get_color_from_hex
from kivy.core.window import Window 

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stencilview import StencilView
from Requ import icon_def
import os
from os.path import join

class Xxuiscreenyy(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
	#def on_kv_post(self, *args):
		
				
class Xxuscreenyy(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
class Xxbarappyy(FloatLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)

class Xxbariconyy(ButtonBehavior, FloatLayout):
	
	text = StringProperty("xml")
	icon = StringProperty("xml")
	ic_color = ColorProperty([0,0,0,1])
	bg_color = ColorProperty([1,1,1,1])
	index = NumericProperty(0)
	
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
	def check(self, args):
		for wid in self.parent.children:
			if args.index == wid.index:
				anim = Animation(
					bg_color=get_color_from_hex("#2196F3") ,
					ic_color=[1,1,1,1], 
					d=0.2,
					).start(wid) 
			else:
				anim = Animation(
					bg_color=[0,0,0,0],
					ic_color=[0,0,0,1],
					d=0.1,
					).start(wid)
					
class Xxcardyy(ButtonBehavior,FloatLayout):
	
	icon = StringProperty("")
	text = StringProperty("")
	sec_text = StringProperty("")
	
	icon_color = ColorProperty([1,1,1,1])
	text_color = ColorProperty([0,0,0,1])

	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
	
class Xxcreateitemyy(BoxLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		Window.softinput_mode = "below_target"

class Xxerrorscreenyy(FloatLayout):
	text = StringProperty("")
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
class Xxiconyy(Label):
	icons = {}
	icon = StringProperty("")
	def __init__(self, **kwargs):
		self.icons = icon_def.icons
		super().__init__(**kwargs)
	
	#def on_kv_post(self,*args):
		
		
		

class Xxraisedbtnyy(ButtonBehavior, FloatLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
class Xxtopappyy(StencilView, FloatLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
