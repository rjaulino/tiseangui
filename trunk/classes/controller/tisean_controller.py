#!/usr/bin/env python

## @package tisean_controller
#  Development Documentation for the tisean_controller package.
#  This package contains all the controller actions to be called from the view layer
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


from tisean_widgets import TiseanCommandMenu
from tisean_widgets import TiseanView
from tisean_factory import TiseanGuiFactory
from tisean_config import TiseanConfig
from tisean_config import TiseanCommandConfig
from tisean_runner import TiseanRunner

##
# Development Documentation for the TiseanController class.
# Represents the main controller of the application that connects the view layer with the model layer.
# The controller is implemented as a mediator between view and model layer.
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanController:

	##
	# The Constructor
	#
	# @param self the instance pointer
	# @param mainInterface the TiseanGuiLauncher instance that controls the view.
	# @param config the TiseanConfig instance that holds the current Tisean configuration
	#
	def __init__(self):


		#building of the configuration
		self.config = TiseanConfig()
		#building of the view
		self.view = TiseanView(self)
		
		#building of command menu option widgets
		tiseanCommandMenu = TiseanCommandMenu(self,self.config)
		self.view.command_menu_setup(tiseanCommandMenu)
				
		#display of the main elements of the view on screen
		self.view.show()

		#we build the command runner
		self.runner = TiseanRunner()
		#we add the observer
		self.runner.register_observer(self.view.get_console_updater())


	##
	# Callback that loads the gui for a certain command on the current view
	#
	# @param self the instance pointer
	# @param menuitem the gui element that made the request
	#
	def load_command_form(self,menuItem):
		
		#we obtain the command configuration
		commandConfig = self.config.get_command_config(menuItem.get_command_name())
		
		factory = TiseanGuiFactory()
		#we build the form
		form = factory.create_form(commandConfig,self)

		#we set it to the view
		self.view.set_command_form(form)
		form.show()
	
	##
	#
	#
	#
	#
	def execute_command(self,button):
	
		#TODO form validation
		form = self.view.get_command_form()
		if (not form.validate()):
			return false
		
		commandString = form.get_command_name()
		
		widgets = form.get_widgets()
		
		for widget in widgets:
			if (widget.get_selected_value() is not ''):
				commandString = commandString + ' ' + widget.get_parameter_name() + ' ' + widget.get_selected_value()

		self.runner.execute_command(commandString)
		
	
	##
	# Closing of application Action
	#
	#
	def application_close(self,window):

		gtk.main_quit()
