#!/usr/bin/env python

## @package tisean_controller
#  Development Documentation for the tisean_controller package.
#  This package contains all the controller actions to be called from the view layer
#

from tisean_widgets import TiseanCommandForm

##
# Development Documentation for the TiseanController class.
# Represents the main controller of the application that connects the view layer with the model layer.
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
	def __init__(self,mainInterface,config):
		self.mainInterface = mainInterface
		self.config = config
	

	##
	# Callback that loads the gui for a certain command on the current view
	#
	# @param self the instance pointer
	# @param menuitem the gui element that made the request
	#
	def load_command_form(self,menuitem):
		form = TiseanCommandForm()
		self.mainInterface.set_command_form(form)
