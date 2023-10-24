import os
import logging

_logger = logging.getLogger()

class Create():
	def __init__(self):
		""" __init__ """
		
		

	def create_wid(self, package, filename):
		path = os.path.join("/sdcard/kiwi", package)
		
		pyfile = f"""from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty,ColorProperty

class {filename.title()}(FloatLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)

"""

		kvfile = f"<{filename.title()}>:" + """
	pos_hint:{"center_x":.5,"center_y":.5}
	canvas.before:
		Color:
			rgba:1,1,1,1
		Rectangle:
			pos:self.pos
			size:self.size
			
	Label:
		color:0,0,0,1 
		text:"widget created successfully"
		halign:"center"

"""
		try:
			filez = os.path.join(path, filename)
			
			if not os.path.exists(filez):
				os.mkdir(filez)
				
			with open(os.path.join(path,f"{filename}",f"{filename}.py"),"w",encoding="utf-8") as pfile:
				
				pfile.write(pyfile)
				pfile.close()
		
			with open(os.path.join(path,f"{filename}",f"{filename}.kv"),"w",encoding="utf-8") as kfile:
				
				kfile.write(kvfile)
				kfile.close()
				
			_logger.info("widget created ")
		except Exception as ex:
			_logger.error(ex)
			
	def create_pro(self, package):
		rfile = """Screen:
	Mainscreen:"""
	
		path = os.path.join("/sdcard/kiwi", package)
		try:
			if not os.path.exists(path):
				os.mkdir(path)
				
			with open(os.path.join(path,"kvroot.kv"),"w",encoding="utf-8") as rootfile:
				
				rootfile.write(rfile)
				rootfile.close()
				
			self.create_wid(package, "mainscreen")
			
			_logger.info("project created ")
		except Exception as ex:
			_logger.error(ex)
	
	
	
