#!/usr/bin/env python


import sys

try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)


class TiseanCommandMenu(gtk.MenuItem):

	def __init__(self,controller,config):
		
		gtk.MenuItem.__init__(self,'commands')
		
		self.controller = controller
		self.config = config
		
		configuredCommands = self.config.get_command_names()
		
		menu = gtk.Menu()
		
		for commandName in configuredCommands:
			item = gtk.MenuItem(commandName)
			item.connect("activate",self.controller.load_command_form)
			item.show()
			menu.add(item)
		
		menu.show()
		
		self.show()
		self.set_submenu(menu)
		
class TiseanCommandForm(gtk.VBox):

	def __init__(self):
	
		gtk.VBox.__init__(self)
		
		#Armado de informacion del comando
		label1 = gtk.Label('label1')
		button1 = gtk.Button('boton1')
		label1.show()
		button1.show()
		label2 = gtk.Label('label2')
		button2 = gtk.Button('boton2')
		label2.show()
		button2.show()
		
		self.pack_end(label1)
		self.pack_end(button1)
		self.pack_end(label2)
		self.pack_end(button2)
		
		self.show()
