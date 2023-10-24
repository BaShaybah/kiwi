__author__ = "Khalid Babiker"

##########################

#from Collection.barapp.barapp import Barapp
#from Collection.baricon.baricon import Baricon
#from Collection.card.card import Card
#from Collection.createitem.createitem import Createitem
#from Collection.icon.icon import Icon
#from Collection.raisedbtn.raisedbtn import Raisedbtn
#from Collection.topapp.topapp import Topapp
#from Collection.uiscreen.uiscreen import Uiscreen
#from Collection.uscreen.uscreen import Uscreen
#from Collection.errorscreen.errorscreen import Errorscreen
from Requ.style import *
##########################

from kivy.app import App
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.logger import Logger
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.clock import Clock, mainthread
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

##########################

import os
from os.path import join
import sys
import importlib

##########################

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent

##########################

from Requ.creator import Create

##########################

class Main(App):
	
	kvRootDir = "/storage/emulated/0/kiwi"
	main_folder = StringProperty("")	
	KVROOT = StringProperty("kvroot.kv")
	
	
	_workingdir = ListProperty([])
	_KVROOT = StringProperty("")
	kvtitle = StringProperty("kiwi")
	
	_grid = None
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		
		
#########################

	def build(self):
		self.mn_sc = Builder.load_file(join(os.getcwd(),"Requ","style.kv"))
		
		self.approot    = None
		self.Vroot = self.mn_sc.ids.view
		
		Window.bind(on_keyboard=self.fast_call)
		return self.mn_sc

#########################
	
	def on_start(self):
		sys.path.append(self.kvRootDir)
		
		return super().on_start()	

	def on_stop(self):
		return super().on_stop()
	def on_pause(self):
		return super().on_pause()
	def on_resume(self):
		return super().on_resume()
	
#########################

	def heat_pro(self,insta):
		
		self.main_folder = insta.text
		self._KVROOT    = join(self.kvRootDir, self.main_folder, self.KVROOT)
				
		self.get_all_paths()
		self.start_watchdog()

		self.hot_start()
		self.mn_sc.ids.sm.current = "view"

#########################
	def update_cards(self,grid):
		
		self._grid = grid
		
		for i in sorted(os.listdir("/sdcard/kiwi")) :
			if os.path.isdir(join("/sdcard/kiwi", i)) :
				sect = f"{i} is project "
				btn = Xxcardyy(
					text=i,
					sec_text=sect,
					icon="layers-edit", 
					icon_color=get_color_from_hex("#2196F3"))
				
				grid.add_widget(btn)
				
#########################

	def create_project(self,package):
		if package.isspace() or package == "":
			return
			
		Create().create_pro(package)
		
		sect = f"{package} is project "
		btn = Xxcardyy(
			text=package,
			sec_text=sect,
			icon="layers-edit",
			icon_color=get_color_from_hex("#2196F3"))
				
		self._grid.add_widget(btn)
		
	
	def create_widget(self,package,filename):
		if package.isspace() or package == "" or filename.isspace() or filename == "" :
			return
			
		Create().create_wid(package, filename)

#########################
			
	def get_all_paths(self):
		self._workingdir = []
		for path, dir, lfile in os.walk(join(self.kvRootDir, self.main_folder)) :
				for mfile in lfile:
					file = join(path, mfile)
					if file.endswith(".py") or file.endswith(".kv") :
						self._workingdir.append(file)
		
		return self._workingdir
			
#########################
			
	def start_watchdog(self):
		try:
			self.event_handler = FileSystemEventHandler()
			self.observer = Observer()
			self.event_handler.dispatch = self.getcheck
			
			for i in self._workingdir:
				self.observer.schedule(self.event_handler, i, recursive=True)
			
			self.observer.start()	
			Clock.schedule_interval(self.getcheck,1)
			
		except Exception as e:
			self.error_view(e)

#########################
			
	@mainthread
	def getcheck(self, event):
		if not isinstance(event, FileModifiedEvent):
			return
			
		kfile = event.src_path
		if kfile != self._KVROOT:
			self.app_reloader(kfile)
		else:
			self.rebuild()

#########################

	def hot_start(self):
		try:
			
			for file in self._workingdir:
				if file.endswith(".py") and file != "__init__.py":
					imp = str(file).split(str(self.kvtitle))[1].replace(os.path.sep,".")
					
					imp = imp.lstrip(".")[:-3]
					cls = str(imp.split(".")[-1])
					
					exec(f"import {imp}")
					importlib.reload(eval(f"{imp}"))
					exec(f"from {imp} import {cls.title()}")

				elif file.endswith(".kv") and file != self._KVROOT:
					Builder.unload_file(file)
					Builder.load_file(file)

			self.rebuild()
			Logger.info(f"{self.kvtitle}: app start")	

		except Exception as e:
			self.error_view(e)
			
#########################

	def unload_app(self):
		
		try:
			for file in self._workingdir:
				if file.endswith(".py"):
					imp = str(file).split(str(self.kvtitle))[1].replace(os.path.sep, ".")
					imp = imp.lstrip(".")[:-3]
					
					cls = str(imp.split(".")[-1])
					
					exec(f"import {imp}")
					importlib.reload(eval(f"{imp}"))
					exec(f"from {imp} import {cls.title()}")
	
					Factory.unregister(f"{cls.title()}")
					
				elif file.endswith(".kv") and file != self._KVROOT:
					Builder.unload_file(file)
			
		except Exception as e:
			self.error_view(e)
	
#########################

	def app_reloader(self, file):
		if file is None:
			return
		try:
			if file.endswith(".py"):
				imp = str(file).split(str(self.kvtitle))[1].replace(os.path.sep, ".")
				imp = imp.lstrip(".")[:-3]
				
				cls = str(imp.split(".")[-1])
				
				exec(f"import {imp}")
				importlib.reload(eval(f"{imp}"))
				exec(f"from {imp} import {cls.title()}")

				Factory.unregister(f"{cls.title()}")
				Factory.register(f"{cls.title()}", eval(f"{cls.title()}"))

			elif file.endswith(".kv") and file != self._KVROOT:
				Builder.unload_file(file)
				Builder.load_file(file)
	
			self.rebuild()
			
		except Exception as e:
			self.error_view(e)
		
#########################

	def error_view(self, txt = ""):
		Logger.error(txt)
		
		self.Vroot.clear_widgets()
		self.Vroot.add_widget(Xxerrorscreenyy(text=str(txt)))

#########################

	def rebuild(self, *args):
		try:
			
			Builder.unload_file(self._KVROOT)
			self.approot = Builder.load_file(self._KVROOT)

			self.Vroot.clear_widgets()
			self.Vroot.add_widget(self.approot)
			Logger.info(f"{self.kvtitle} : app reloaded")
			
		except Exception as e:
			self.error_view(e)
			
#########################
	
	def fast_call(self,*args):
		
		if args[1] == 27:
			if self.mn_sc.ids.sm.current == "view":
				self.unload_app()
				self.mn_sc.ids.sm.current = "uiscreen"
				try:
					self.observer.stop()
					
				except Exception as e:
					return self.fast_call
		
		return self.fast_call
		
#########################

if __name__ == "__main__":
	Main().run()