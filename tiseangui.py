#!/usr/bin/env python

import sys

sys.path.append('classes/gui/')
sys.path.append('classes/controller/')
sys.path.append('classes/config/')
sys.path.append('config/')

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
	
from tisean_widgets import TiseanCommandMenu
from tisean_controller import TiseanController
from tisean_config import TiseanConfig

## @package tisean_launcher
#  Development Documentation for the tisean_launcher package.
#  This package contains the launcher for the application
#

##
# Development Documentation for the TiseanGuiLauncher class.
# Represents the launcher of the Application
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanGuiLauncher:

	##
	# The Constructor
	#
	# @param self the instance pointer
	#
	def __init__(self):
		
		#Set the Glade file
		self.gladefile = "classes/gui/glade/tiseangui.glade"
		  
		self.currentForm = None
		self.mainInterface = gtk.glade.XML(self.gladefile)
		self.mainWindow = self.mainInterface.get_widget("TiseanGUI")
		self.consoleWindow = self.mainInterface.get_widget("TiseanGuiConsole")
		self.menuBar = self.mainInterface.get_widget("TiseanMenuBar")
		self.optionsCommandsHolder = self.mainInterface.get_widget("TiseanCommandOptionsHolder")
		self.config = TiseanConfig()		
		self.controller = TiseanController(self,self.config)
		
		self.mainWindow.show()
		self.consoleWindow.show()
		
		if (self.mainWindow):
			self.mainWindow.connect("destroy",gtk.main_quit)

		#armado de opciones de menu de comandos
		menuHolderItem = TiseanCommandMenu(self.controller,self.config)
		self.menuBar.append(menuHolderItem)

	##
	# Sets the configuration form of a command on the main gui.
	#
	# @param self the instance pointer
	# @param form TiseanCommandForm instance
	#		
	def set_command_form(self,form):
		if (self.currentForm):
			self.optionsCommandsHolder.remove(self.currentForm)
		self.optionsCommandsHolder.pack_end(form)
		self.currentForm = form

if __name__ == "__main__":
	tiseanGui = TiseanGuiLauncher()
	gtk.main()
