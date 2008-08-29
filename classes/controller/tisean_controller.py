#!/usr/bin/env python

from tisean_widgets import TiseanCommandForm

class TiseanController:

	def __init__(self,mainInterface,config):
		self.mainInterface = mainInterface
		self.config = config
	

	def load_command_form(self,menuitem):
		form = TiseanCommandForm()
		self.mainInterface.set_command_form(form)
