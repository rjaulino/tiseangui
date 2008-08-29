#!/usr/bin/env python

import sys
from xml.dom.minidom import parse

class TiseanCommandConfig:

	def __init__(self,name,commandLineName):
		self.name = name
		self.commandLineName = commandLineName
	
	def get_name(self):
		return self.name
		
	def get_command_line_name(self):
		return self.commandLineName


class TiseanConfig:	

	def __init__(self):
		self.configDom = parse('config/tisean-command-config.xml')
		self.commandNames = []
		self.commands = {}

		commandNodes = self.configDom.getElementsByTagName("command")

		for commandNode in commandNodes:
		
			#we build and instance of TiseanCommandConfig
			nameNode = commandNode.getElementsByTagName("name")[0]
			for node in nameNode.childNodes:
				if (node.nodeType == node.TEXT_NODE):
					name = node.data
					self.commandNames.append(node.data)
			
			commandNameNode = commandNode.getElementsByTagName("commandLineName")[0]
			for node in commandNameNode.childNodes:
				if (node.nodeType == node.TEXT_NODE):
					commandName = node.data

			commandConfig = TiseanCommandConfig(name,commandName)
			self.commands[name] = commandConfig

		
	def get_command_names(self):
		return self.commandNames
		
	def get_command_config(self,commandName):
		return self.commands[commandName]

