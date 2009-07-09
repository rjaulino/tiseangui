#!/usr/bin/env python

import sys

sys.path.append('classes/gui/')
sys.path.append('classes/runner/')
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
	import platform
	if (platform.system() is not 'Windows'):
		gtk.gdk.threads_init()
	#Initializing the gtk's thread engine

except:
	sys.exit(1)
	
from tisean_controller import TiseanController

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
		self.controller = TiseanController()


if __name__ == "__main__":
	tiseanGui = TiseanGuiLauncher()
	gtk.main()
