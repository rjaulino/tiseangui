#!/usr/bin/env python

## @package tisean_widgets
#  Development Documentation for the tisean_widgets package.
#  This package contains all classes that represent, create and manipulate the gui widget of the application
#

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

##
# Development Documentation for the TiseanCommandMenu class.
# Represents the tisean commands menu widget
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanCommandMenu(gtk.MenuItem):

	##
	# The Constructor
	#
	# @param self the instance pointer
	# @param the TiseanController instance
	# @param config the TiseanConfig instance that holds the current Tisean configuration
	#	
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

##
# Development Documentation for the TiseanCommandForm class.
# Represents the tisean commands form widget
# @author Martin Ramos Mejia
# @version 0.1
#		
class TiseanCommandForm(gtk.VBox):

	##
	# The Constructor
	#
	# @param self the instance pointer
	#
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
