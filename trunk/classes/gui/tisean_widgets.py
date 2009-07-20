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

import platform

from tisean_view_updater import TiseanViewUpdater

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
		self.consoleMenuItem = self.mainInterface.get_widget("console1")
		self.aboutUsDialog = self.mainInterface.get_widget('TiseanGuiAbout');
		
		self.consoleWindow.hide()
		self.aboutUsDialog.hide()
		
		# we set updater method that process the messages that receives the console
		self.consoleUpdater = TiseanViewUpdater(self.consoleWindow)
		# we start the updater
		self.consoleUpdater.start_updater()
				
		#we connect the callbacks of the view
		self.callback_connection()


	##
	# Setup of the command menu of the main view
	#
	# @param self the instance pointer
	# @param TiseanCommandMenu command menu widget
	#	
	def command_menu_setup(self,tiseanCommandMenu):
		self.menuBar.insert(tiseanCommandMenu,2)


	##
	# Callback to Hide the ConsoleWindow
	#
	# @param self the instance pointer
	#
	def console_hide(self, widget, event):
		self.consoleWindow.hide()
		return True
		
	##
	# Callback to Show the ConsoleWindow
	#
	# @param self the instance pointer
	#
	def console_show(self, widget, event):
		self.consoleWindow.show()
		return True

	##
	# Shows the ConsoleWindow
	#
	# @param self the instance pointer
	#
	def console_show(self):
		self.consoleWindow.show()
		return True

	
	##
	# Connects all the callbacks of the main elements of the view
	#
	# @param self the instance pointer	
	def callback_connection(self):

		if (self.mainWindow):
			self.mainWindow.connect("destroy",self.controller.application_close)

		#we prevent the console window to be destroyed
		if (self.consoleWindow):
			self.consoleWindow.connect("delete-event",self.console_hide)

		#we prevent the about us dialog to be destroyed
		if (self.aboutUsDialog):
			self.aboutUsDialog.connect("delete-event",self.about_dialog_hide)
			self.aboutUsDialog.connect("close",self.about_dialog_hide)
		
		#menu items callbacks

		# console display
		if (self.consoleMenuItem):
			self.consoleMenuItem.connect("activate",self.console_display)
			
		# exit from file menu
		quitMenuItem = self.mainInterface.get_widget("quit1")
		if (quitMenuItem):
			quitMenuItem.connect("activate",self.controller.application_close)

		#about us display
		aboutUsMenuItem = self.mainInterface.get_widget("about1")
		if (aboutUsMenuItem):
			aboutUsMenuItem.connect("activate",self.about_dialog_show)
		
		return True
	
	##
	# Callback to show the About Dialog on the GUI
	#
	# @param self the instance pointer
	# @param menuItem widget that performs the calling
	#
	def about_dialog_show(self,menuItem):
		self.aboutUsDialog.show()
		return True

	##
	# Callback to hide the About Dialog on the GUI
	#
	# @param self the instance pointer
	#		
	def about_dialog_hide(self, widget, event):
		self.aboutUsDialog.hide()
		return True

	##
	# Callback to show the Console Dialog on the GUI
	#
	# @param self the instance pointer
	# @param menuItem widget that performs the calling
	#
	def console_display(self,menuItem):

		if (self.consoleWindow.get_property("visible")):
			self.consoleWindow.hide()
		else:
			self.consoleWindow.show()
			
	##
	# Shows the main elements controlled by the view
	#
	# @param self the instance pointer	
	def show(self):
		self.mainWindow.show()
		
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
		self.optionsCommandsHolder.set_border_width(10)
		self.currentForm = form
	
	##
	# Getter of the current command form
	# 
	# @param self the instance pointer
	#
	def get_command_form(self):
		return self.currentForm
	
	##
	# Getter of the Console updater of the View
	#
	# @param self the instance pointer
	#
	def get_console_updater(self):
		return self.consoleUpdater
	
	##
 	# Stops the Console updater of the view
	#
	# @param self the instance pointer
	#
	def stop_console_updater(self):
		self.consoleUpdater.stop_updater()

##
# Represents a menu item of the Tisean GUI 
# 
# @author Martin Ramos Mejia
# @version 0.1
class TiseanMenuItem(gtk.MenuItem):

	##
	# The constructor
	#
	# @param self the instance pointer
	# @param name the name of the menu item
	def __init__(self,name):
		gtk.MenuItem.__init__(self,name)
		self.commandName = name
	
	##
	# Getter of the menu item name
	#
	# @param self the instance pointer
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
		
		gtk.MenuItem.__init__(self,'Commands')
		
		self.controller = controller
		self.config = config
		
		configuredCommands = self.config.get_command_names()
		
		menu = gtk.Menu()
		subsections = {}

		for commandName in configuredCommands:
			item = TiseanMenuItem(commandName)
			item.connect("activate",self.controller.load_command_form)
			item.show()
						
			commandConfig = self.config.get_command_config(commandName)
			section = commandConfig.get_section()
			if (section is not None):
				if (not subsections.has_key(section)):
					sectionElement = gtk.MenuItem(section)
					sectionElement.show()
					subsections[section] = sectionElement
					sectionMenuElement = gtk.Menu()
					sectionElement.set_submenu(sectionMenuElement)
					sectionMenuElement.show()
					menu.add(sectionElement)
				else:
					sectionElement = subsections[section]
					sectionMenuElement = sectionElement.get_submenu()

				sectionMenuElement.add(item)
			else:
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
		self.set_homogeneous(True);
		self.controller = controller		
		self.commandName = name
		self.label = gtk.Label(self.commandName)
		self.label.set_markup('<big><b>' + self.commandName + '</b></big>')		
		self.widgets = widgets
		self.messageBox = gtk.Label()
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
	# Displays the command form
	#
	# @param self the instance pointer
	#	
	def show(self):
		
		self.pack_start(self.label,False,False)
		self.label.show()
		
		for widget in self.widgets:
			self.pack_start(widget,False,False)
			widget.show()

		commandHolder = gtk.HBox()
		commandHolder.pack_start(self.executeButton,False,False)
		commandHolder.pack_start(self.messageBox,False,False)
		commandHolder.show()

		self.pack_start(commandHolder,False,False)
		
		self.executeButton.show()
		self.messageBox.show()
				
		gtk.VBox.show(self)
	
	##
	# Validates the current form
	#
	# @return boolean True if valid, False if invalid
	def validate(self):

		#required widgets validation
		invalid = []
		for widget in self.widgets:
			if ((widget.get_selected_value() is '') and (widget.is_required())):
				invalid.append(widget)
				
		if (len(invalid) is 0):
			return True

		for widget in invalid:
			widget.set_invalid_layout()
		#there were invalid items
		return False
	
	##
	# Getter of the command that the form represents
	# 
	# @param self the instance pointer
	#				
	def get_command_name(self):
		command = self.commandName
		if (platform.system() is 'Windows'):
			command = command + '.exe' 
		return command
	
	##
	# Getter of all the parameter widgets included in the Form
	#
	# @param self the instance pointer
	#
	def get_widgets(self):
		return self.widgets
	
	##
	# Deletes all the validation errors from the GUI
	#
	# @param self the instance pointer
	#	
	def clear_validation_errors(self):
		self.clear_message_box()
		for	widget in self.widgets:
			widget.set_valid_layout()

	##
	# Sets a message in the message box of the form
	#
	# @param self the instance pointer
	# @param text text to be set in the message box
	#
	def set_message_in_message_box(self,text):
		return self.messageBox.set_markup('<b>' + text + '</b>')
	
	##
	# Clears the content of the message box of the form
	#
	# @param self the instance pointer
	#	
	def clear_message_box(self):
		return self.messageBox.set_text('')

##
# Base interface that describes a TiseanWidget
# 
# @author Martin Ramos Mejia
# @version 0.1	
class TiseanWidget:
	
	##
	# The Constructor 
	# 
	# @param self The instance pointer
	# @param name name of the widget
	#
	def __init__(self,name):
		self.parameterName = name
		self.required = False
	
	##
	# Validates the widget
	#
	# @param self The instance pointer
	#
	def validate(self):
		return True

	##
	# Getter of the parameter name represented on the widget
	#
	# @param self The instance pointer
	#		
	def get_parameter_name(self):
		return self.parameterName

	##
	# Getter of the current value of the widget
	#
	# @param self The instance pointer
	#		
	def get_selected_value(self):
		return '0'
	
	##
	# Sets the widget as a required parameter
	#
	# @param self The instance pointer
	#			
	def set_required(self):
		self.required = True

	##
	# Indicates of the widget is a required parameter or not
	#
	# @param self The instance pointer
	#		
	def is_required(self):
		return self.required

	##
	# Defines the invalid layout of the widget
	#
	# @param self The instance pointer
	#			
	def set_invalid_layout(self):
		pass

	##
	# Defines a valid layout over the widget
	#
	# @param self The instance pointer
	#		
	def set_valid_layout(self):
		pass

	##
	# Translates the current values of the widget to a parameter string to form an execution string
	#
	# @param self The instance pointer
	#		
	def get_parameter_string(self):
		if (self.get_selected_value() is not ''):
			return self.get_parameter_name() + ' ' + self.get_selected_value()
		else:
			return ''
				
##
# File Widget Dialog
# 
# @author Martin Ramos Mejia
# @version 0.1				
class TiseanFileDialogWidget(TiseanWidget,gtk.FileChooserDialog):

	##
	# The Constructor
	#
	# @param self The instance pointer
	# @param tiseanFileWidget file widget related to the dialog
	#
	def __init__(self,tiseanFileWidget):
		self.tiseanFileWidget = tiseanFileWidget
		gtk.FileChooserDialog.__init__(self);
		self.callback_connections()

	##
	# Connects the callbacks of the widget
	#
	# @param self The instance pointer
	#			
	def callback_connections(self):
		self.connect('file-activated',self.update_file_widget)

	##
	# Performs the update of the tiseanFileWidget related to the TiseanFileDialogWidget
	#
	# @param self The instance pointer
	#			
	def update_file_widget(self,filechooser):
		self.hide()
		self.tiseanFileWidget.change_selected_file(self.get_filename())
			
		
##
# File Widget
# 
# @author Martin Ramos Mejia
# @version 0.1
class TiseanFileWidget(TiseanWidget,gtk.HBox):

	##
	# The Constructor
	#
	# @param self The instance pointer
	#		
	def __init__(self,name,label):
		TiseanWidget.__init__(self,name)
		gtk.HBox.__init__(self)
		self.set_spacing(5)					
		self.label = gtk.Label()
		self.label.set_markup('<b>' + label + '</b>')		
		self.label.set_single_line_mode(True)
		self.entry = gtk.Entry()
		self.entry.set_editable(True)
		self.button = gtk.Button('Select a File');
		self.callback_connection()
		
	##
	# Connects all the callbacks
	#
	# @param self the instance pointer	
	def callback_connection(self):
		self.button.connect('clicked',self.display_file_dialog)

	##
	# Shows the file dialog
	#
	# @param self The instance pointer
	#				
	def display_file_dialog(self,button):
		self.fileDialog = TiseanFileDialogWidget(self);
		self.fileDialog.show()
		
	##
	# Changes the selected file on the widget
	#
	# @param self The instance pointer
	#				
	def change_selected_file(self,fileRoute):
		self.entry.set_text(fileRoute)
	
	##
	# shows the widget
	#
	# @param self The instance pointer
	#				
	def show(self):
		self.pack_start(self.label,False,False)
		self.pack_start(self.entry,False,False)
		self.pack_start(self.button,False,False)
		self.label.show()
		self.entry.show()
		self.button.show()
		gtk.VBox.show(self)
		
	##
	# Returns the current value of the widget
	#
	# @param self The instance pointer
	#						
	def get_selected_value(self):
		return self.entry.get_text()

	##
	# Sets the invalid layout  
	#
	# @param self The instance pointer
	#						
	def set_invalid_layout(self):
		colour = gtk.gdk.color_parse('red3')
		self.entry.modify_base(gtk.STATE_NORMAL,colour)

	##
	# Sets the valid layout of the widget
	# 
	# @param self The instance pointer
	#						
	def set_valid_layout(self):
		colour = gtk.gdk.color_parse('white')
		self.entry.modify_base(gtk.STATE_NORMAL,colour)		

##
# Text Parameter Widget
# 
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanTextParameterWidget(TiseanWidget,gtk.HBox):

	##
	# Constructor
	#
	# @param self The instance pointer
	#				
	def __init__(self,name,label):
		TiseanWidget.__init__(self,name)
		gtk.HBox.__init__(self)
		self.set_spacing(5)				
		self.label = gtk.Label()
		self.label.set_markup('<b>' + label + '</b>')
		self.label.set_single_line_mode(True)
		self.entry = gtk.Entry()
		self.entry.set_max_length(50)

	##
	# Displays the widget
	#
	# @param self The instance pointer
	#
	def show(self):
		self.pack_start(self.label,False,False)
		self.pack_start(self.entry,False,False)
		self.label.show()
		self.entry.show()
		gtk.VBox.show(self)

	##
	# Obtains the selected value of the widget 
	#
	# @param self The instance pointer
	#				
	def get_selected_value(self):
		return self.entry.get_text()

	##
	# Sets the invalid layout
	# 
	# @param self The instance pointer
	#				
	def set_invalid_layout(self):
		colour = gtk.gdk.color_parse('red3')
		self.entry.modify_base(gtk.STATE_NORMAL,colour)

	##
	# Sets the valid layout
	#
	# @param self The instance pointer
	#				
	def set_valid_layout(self):
		colour = gtk.gdk.color_parse('white')
		self.entry.modify_base(gtk.STATE_NORMAL,colour)		

##
# Parameter with Options Widget
# 
# @author Martin Ramos Mejia
# @version 0.1
class TiseanOptionsParameterWidget(TiseanWidget,gtk.HBox):

	##
	# The Constructor
	#
	# @param self The instance pointer
	#				
	def __init__(self,name,label,options):
		TiseanWidget.__init__(self,name)
		gtk.HBox.__init__(self)
		self.set_spacing(10)	
		self.label = gtk.Label()
		self.label.set_markup('<b>' + label + '</b>')
		self.label.set_single_line_mode(True)
		self.radioHolder = gtk.HBox(False, 0)
		self.buttons = []
		
		first = None
		
		for option in options:
			
			if (first is not None):
				button = gtk.RadioButton(first, option)

			if (first is None):
				button = gtk.RadioButton(None, option)
				first = button
				
			self.radioHolder.pack_start(button, False, False, 0)
			self.buttons.append(button)
			button.show()
			
	##
	# Displays the widget
	#
	# @param self The instance pointer
	#					
	def show(self):
		self.pack_start(self.label,False,False)
		self.pack_start(self.radioHolder,False,False)
		self.label.show()
		self.radioHolder.show()
		gtk.VBox.show(self)
		
	##
	# Returns the current value of the widget
	#
	# @param self The instance pointer
	#						
	def get_selected_value(self):
		
		for button in self.buttons:
			if (button.get_active() is True):
				return button.get_label()

##
# Simple Parameter Widget
# 
# @author Martin Ramos Mejia
# @version 0.1
class TiseanSimpleParameterWidget(TiseanOptionsParameterWidget):

	##
	# The Constructor
	#
	# @param self The instance pointer
	#				
	def __init__(self,name,label):
		options = ['no', 'yes']
		TiseanOptionsParameterWidget.__init__(self,name,label,options)

	##
	# Returns the processed parameter string 
	#
	# @param self The instance pointer
	#				
	def get_parameter_string(self):
		value = self.get_selected_value()
		if (value == 'yes'):
			return self.get_parameter_name()
		else:
			return ''
