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

from tisean_view_updater import TiseanViewSimpleUpdater

##
# Represents the main view of the Tisean Gui, and 
# controls of the widgets of the gui
# @author Martin Ramos Mejia
# @version 0.1
class TiseanView():

	##
	# The Constructor
	#
	# @param self the instance pointer
	#	
	def __init__(self,controller):
		
		#Set the Glade file
		self.gladefile = "classes/gui/glade/tiseangui.glade"
		  
		self.controller = controller
		self.currentForm = None
		# we load the main widgets of the view
		self.mainInterface = gtk.glade.XML(self.gladefile)
		self.mainWindow = self.mainInterface.get_widget("TiseanGUI")
		self.consoleWindow = self.mainInterface.get_widget("TiseanGuiConsole")
		self.menuBar = self.mainInterface.get_widget("TiseanMenuBar")
		self.optionsCommandsHolder = self.mainInterface.get_widget("TiseanCommandOptionsHolder")
		
		# we start the thread that process the messages that receives the console
		self.consoleUpdater = TiseanViewSimpleUpdater(self.consoleWindow)
				
		#we connect the callbacks of the view
		self.callback_connection()


	##
	# Setup of the command menu of the main view
	#
	# @param self the instance pointer
	# @param TiseanCommandMenu command menu widget
	#	
	def command_menu_setup(self,tiseanCommandMenu):
		self.menuBar.append(tiseanCommandMenu)

	
	##
	# Connects all the callbacks of the main elements of the view
	#
	# @param self the instance pointer	
	def callback_connection(self):

		if (self.mainWindow):
			self.mainWindow.connect("destroy",self.controller.application_close)

	##
	# Shows the main elements controlled by the view
	#
	# @param self the instance pointer	
	def show(self):
		
		self.mainWindow.show()
	#	self.consoleWindow.show()	
		
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
	
	def get_command_form(self):
		return self.currentForm
	
	##
	#
	#
	#
	def get_console_updater(self):
		return self.consoleUpdater
	
	##
	#
	#
	#
	def stop_console_updater(self):
		self.consoleUpdater.stop_updater()

class TiseanMenuItem(gtk.MenuItem):

	def __init__(self,name):
		gtk.MenuItem.__init__(self,name)
		self.commandName = name
	
	def get_command_name(self):
		return self.commandName
		

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
			item = TiseanMenuItem(commandName)
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
	# @param name name of the command that the form represents
	# @param widgets array of TiseanWidget instances
	#
	def __init__(self,name,widgets,controller):
	
		gtk.VBox.__init__(self)
		self.controller = controller		
		self.commandName = name
		self.label = gtk.Label(self.commandName)
		self.widgets = widgets
		self.executeButton = gtk.Button('Execute Command')
		self.set_spacing(10)
		self.callback_connection()
		
	##
	# Connects all the callbacks of the main elements of the view
	#
	# @param self the instance pointer	
	def callback_connection(self):
		self.executeButton.connect('clicked',self.controller.execute_command)
	
	##
	#
	#
	#	
	def show(self):
		
		self.pack_start(self.label,False,False)
		self.label.show()
		
		for widget in self.widgets:
			self.pack_start(widget,False,False)
			widget.show()

		self.pack_start(self.executeButton,False,False)
		self.executeButton.show()

		gtk.VBox.show(self)
	
	##
	# Validates the current form
	# @todo
	#
	def validate(self):
		
		return True
	
	def get_command_name(self):
		return self.commandName
	
	def get_widgets(self):
		return self.widgets

class TiseanWidget:
	
	def __init__(self,name):
		self.parameterName = name
	
	def validate(self):
		return True
		
	def get_parameter_name(self):
		return self.parameterName

	def get_selected_value(self):
		return '0'
				
class TiseanFileDialogWidget(TiseanWidget,gtk.FileChooserDialog):

	def __init__(self,tiseanFileWidget):
		self.tiseanFileWidget = tiseanFileWidget
		gtk.FileChooserDialog.__init__(self);
		self.callback_connections()
	
	def callback_connections(self):
		self.connect('file-activated',self.update_file_widget)
	
	def update_file_widget(self,filechooser):
		self.hide()
		self.tiseanFileWidget.change_selected_file(self.get_filename())
			
		

class TiseanFileWidget(TiseanWidget,gtk.VBox):

	def __init__(self,name,label):
		TiseanWidget.__init__(self,name)
		gtk.VBox.__init__(self)	
		self.label = gtk.Label(label)
		self.label.set_single_line_mode(True)
		self.entry = gtk.Entry()
		self.entry.set_editable(False)
		self.button = gtk.Button('Select a File');
		self.callback_connection()
		
	##
	# Connects all the callbacks of the main elements of the view
	#
	# @param self the instance pointer	
	def callback_connection(self):
		self.button.connect('clicked',self.display_file_dialog)
		
	def display_file_dialog(self,button):
		self.fileDialog = TiseanFileDialogWidget(self);
		self.fileDialog.show()
		
	def change_selected_file(self,fileRoute):
		self.entry.set_text(fileRoute)
	
	def show(self):
		self.pack_start(self.label,False,False)
		self.pack_start(self.entry,False,False)
		self.pack_start(self.button,False,False)
		self.label.show()
		self.entry.show()
		self.button.show()
		gtk.VBox.show(self)
		

class TiseanIntegerParameterWidget(TiseanWidget,gtk.VBox):

	def __init__(self,name,label):
		TiseanWidget.__init__(self,name)
		gtk.VBox.__init__(self)
		self.label = gtk.Label(label)
		self.label.set_single_line_mode(True)
		self.entry = gtk.Entry()
		self.entry.set_max_length(50)
		
	
	def show(self):
		self.pack_start(self.label,False,False)
		self.pack_start(self.entry,False,False)
		self.label.show()
		self.entry.show()
		gtk.VBox.show(self)

	def get_selected_value(self):
		return self.entry.get_text()
		

class TiseanOptionsParameterWidget(TiseanWidget,gtk.VBox):

	def __init__(self,name,label,options):
		TiseanWidget.__init__(self,name)
		gtk.VBox.__init__(self)	
		self.label = gtk.Label(label)
		self.label.set_single_line_mode(True)
		self.radioHolder = gtk.HBox(False, 0)
		
		first = None
		
		for option in options:

			if (first is not None):
				button = gtk.RadioButton(first, option)

			if (first is None):
				button = gtk.RadioButton(None, option)
				first = button
				
			self.radioHolder.pack_start(button, False, False, 0)
			button.show()
			
	
	def show(self):
		self.pack_start(self.label,False,False)
		self.pack_start(self.radioHolder,False,False)
		self.label.show()
		self.radioHolder.show()
		gtk.VBox.show(self)
