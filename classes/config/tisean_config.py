#!/usr/bin/env python

## @package tisean_config
#  Development Documentation for the tisean_config package.
#

import sys
from xml.dom.minidom import parse
from tisean_strategy import TiseanGuiParameterBuildStrategy
from tisean_strategy import TiseanGuiTextParameterBuildStrategy
from tisean_strategy import TiseanGuiOptionsParameterBuildStrategy
from tisean_strategy import TiseanGuiFileParameterBuildStrategy
from tisean_strategy import TiseanGuiSimpleParameterBuildStrategy

##
# Development Documentation for the TiseanCommandConfig class.
# Represents the configuration of a Tisean Command.
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanCommandConfig:
	
	##
	# The Constructor
	#
	# @param self the instance pointer
	# @param name command name
	# @param commandLineName name that the command has on command line
	#
	def __init__(self,name,commandLineName):
		self.name = name
		self.commandLineName = commandLineName
		self.parameters = {}
		self.section = None
		self.noinput = False
	
	##
	# Getter for the name of the command
	# 
	# @param self the instance pointer
	# @return string the name of the command
	#
	def get_name(self):
		return self.name
	
	##
	# Getter for the name of the command on command line
	# 
	# @param self the instance pointer
	# @return string the name of the command on command line
	#	
	def get_command_line_name(self):
		return self.commandLineName
		
	
	##
	# Adds a TiseanCommandParameterConfig instance to the current command
	# 
	# @param self the instance pointer
	# @param parameter instance of TiseanCommandParameterConfig
	#	
	def add_parameter(self,parameter):
		self.parameters[parameter.get_value()] = parameter
		
	##
	#
	#
	#
	#
	def get_parameters(self):
		return self.parameters

	##
	# Sets the section of the command.
	#
	# @param self the instance pointer
	# @return String or None
	def set_section(self,section):	
		self.section = section
	
	##
	# Returns the section of the command.
	#
	# @param self the instance pointer
	# @return String or None
	def get_section(self):
		if (self.section is ''):
			return None
		return self.section
	
	##
	# sets the command to dont have input support input
	#
	def set_no_input(self):
		self.noinput = True
	
	def has_input(self):
		return not self.noinput

##
# Development Documentation for the TiseanCommandParameterConfig class.
# Represents the configuration of a Tisean Command Parameter.
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanCommandParameterConfig:

	##
	# The Constructor
	#
	# @param self the instance pointer
	# @param name command parameter name
	# @param value command parameter value
	#
	def __init__(self,name,value):
		self.name = name
		self.value = value
		self.required = False
		
	##
	# Getter for the value of the command parameter
	# 
	# @param self the instance pointer
	# @return string the name of the command on command line
	#
	def get_value(self):
		return self.value

	##
	# Getter for the name of the command parameter
	# 
	# @param self the instance pointer
	# @return string the name of the command on command line
	#		
	def get_name(self):
		return self.name
	
	##
	# Makes the parameter a required parameter for the command
	#
	def set_required(self):
		self.required = True
		
	##
	# Indicates if a parameter is required
	#
	def is_required(self):
		return self.required
		
	##
	# Returns the build strategy of the GUI Element that represents the parameter
	#
	def get_build_strategy(self):
		pass
	

#
# Subclass that defines a Parameter that accepts only text.
# 
#		
class TiseanCommandParameterText(TiseanCommandParameterConfig):

	##
	# The Constructor
	#
	# @param self the instance pointer
	# @param name command name
	# @param commandLineName name that the command has on command line
	#
	def __init__(self,name,commandLineName):
		TiseanCommandParameterConfig.__init__(self,name,commandLineName)

	##
	# Returns the build strategy of the GUI Element that represents the parameter
	#
	def get_build_strategy(self):
		return TiseanGuiTextParameterBuildStrategy()

#
# Subclass that defines a Simple parameter (no value).
# 
#		
class TiseanCommandParameterSimple(TiseanCommandParameterConfig):

	##
	# The Constructor
	#
	# @param self the instance pointer
	# @param name command name
	# @param commandLineName name that the command has on command line
	#
	def __init__(self,name,commandLineName):
		TiseanCommandParameterConfig.__init__(self,name,commandLineName)

	##
	# Returns the build strategy of the GUI Element that represents the parameter
	#
	def get_build_strategy(self):
		return TiseanGuiSimpleParameterBuildStrategy()
		

#
# Subclass that defines a Parameter that its a file dialog.
# 
#		
class TiseanCommandParameterFile(TiseanCommandParameterConfig):

	##
	# The Constructor
	#
	# @param self the instance pointer
	# @param name command name
	# @param commandLineName name that the command has on command line
	#
	def __init__(self,name,commandLineName):
		TiseanCommandParameterConfig.__init__(self,name,commandLineName)

	##
	# Returns the build strategy of the GUI Element that represents the parameter
	#
	def get_build_strategy(self):
		return TiseanGuiFileParameterBuildStrategy()

		
#
# Subclass that defines a Parameter that accepts different options.
# 
#		
class TiseanCommandParameterOptions(TiseanCommandParameterConfig):

	##
	# The Constructor
	#
	# @param self the instance pointer
	# @param name command name
	# @param commandLineName name that the command has on command line
	#
	def __init__(self,name,commandLineName):
		TiseanCommandParameterConfig.__init__(self,name,commandLineName)
		self.options = []

	##
	# Adds and option to the dictionary of options.
	# The options are a simple string.
	# @param self the instance pointer
	# @param option the string option
	#
	def add_option(self,option):
		self.options.append(option)
	
	##
	# Returns all the options for the parameter
	#
	#
	def get_options(self):
		return self.options

	##
	# Returns the build strategy of the GUI Element that represents the parameter
	#
	def get_build_strategy(self):
		return TiseanGuiOptionsParameterBuildStrategy()

##
# Development Documentation for the TiseanConfig class.
# Represents the configuration of the current Tisean Package
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanConfig:	

	##
	# The Constructor
	#
	# @param self the instance pointer
	#
	def __init__(self):
		self.configDom = parse('config/tisean-command-config.xml')
		self.commandNames = []
		self.commands = {}

		commandNodes = self.configDom.getElementsByTagName("command")

		for commandNode in commandNodes:
			#for every command
			#we process its config info
			
			noinputAtt = commandNode.getAttribute('noinput')
			if (noinputAtt is not '' and noinputAtt == 'true'):
				noinput = True
			else:
				noinput = False
			
			nameNode = commandNode.getElementsByTagName("name")[0]
			for node in nameNode.childNodes:
				if (node.nodeType == node.TEXT_NODE):
					name = node.data
					self.commandNames.append(node.data)
			
			commandNameNode = commandNode.getElementsByTagName("commandLineName")[0]
			for node in commandNameNode.childNodes:
				if (node.nodeType == node.TEXT_NODE):
					commandName = node.data

			section = ''
			sectionHolder = commandNode.getElementsByTagName("section")[0]
			if (sectionHolder is not ''):
				for node in sectionHolder.childNodes:
					if (node.nodeType == node.TEXT_NODE):
						section = node.data
			
			#we create an instance of TiseanCommandConfig that represents the command
			commandConfig = TiseanCommandConfig(name,commandName)
			if (noinput):
				commandConfig.set_no_input()
				
			commandConfig.set_section(section)
			self.commands[name] = commandConfig

			#we process the parameters of the command
			parametersNode = commandNode.getElementsByTagName("parameters")[0]
			parameterList = parametersNode.getElementsByTagName("parameter")
			for paramNode in parameterList:
				#for every parameter
				
				#required checkup
				requiredAtt = paramNode.getAttribute('required')
				if (requiredAtt is not '' and requiredAtt == 'true'):
					required = True
				else:
					required = False

				paramNameNode = paramNode.getElementsByTagName("name")[0]
				for node in paramNameNode.childNodes:
					if (node.nodeType == node.TEXT_NODE):
						paramName = node.data
				
				paramValueNode = paramNode.getElementsByTagName("value")[0]
				for node in paramValueNode.childNodes:
					if (node.nodeType == node.TEXT_NODE):
						paramValue = node.data
	
				#we process the parameter type				
				paramValueNode = paramNode.getElementsByTagName("type")[0]
				for node in paramValueNode.childNodes:
					if (node.nodeType == node.TEXT_NODE):
						paramType = node.data

				if paramType == 'text':
					parameterConfig = TiseanCommandParameterText(paramName,paramValue)
				
				if paramType == 'options':
					parameterConfig = TiseanCommandParameterOptions(paramName,paramValue)
					
					#we process the options
					optionsNode = paramNode.getElementsByTagName("options")[0]
					optionList = optionsNode.getElementsByTagName("option")

					for optionNode in optionList:
						optionTextNode = optionNode.childNodes[0]
						if (optionTextNode.nodeType == optionTextNode.TEXT_NODE): 
							value = optionTextNode.data
							parameterConfig.add_option(value)
				
				if paramType == 'file':
					parameterConfig = TiseanCommandParameterFile(paramName,paramValue)
					
				if paramType == 'simple':
					parameterConfig = TiseanCommandParameterSimple(paramName,paramValue)
					
				
				#we set the parameter as required if so.
				if (required is True):
					parameterConfig.set_required()
					
				#we add it to the command config instance
				commandConfig.add_parameter(parameterConfig)
		
	##
	# Method that returns a list of all the commands supported
	#
	# @param self the instance pointer
	# @param name command parameter name
	# @param value command parameter value
	#
	def get_command_names(self):
		return self.commandNames

	##
	# Method that returns the TiseanCommandConfig instance for a certain command
	#
	# @param self the instance pointer
	# @param commandName The name of the command we want to obtain the TiseanCommandConfig instance
	# @return TiseanCommandConfig instance
	#			
	def get_command_config(self,commandName):
		return self.commands[commandName]

