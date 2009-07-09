import sys
import os
import time
import subprocess
import tempfile
from subprocess import Popen,PIPE
from threading import Thread

##
# Thread that runs a certain command and updates a number of observers on runtime
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanRunner(Thread):

	##
	# The Constructor
	# @param self the instance pointer
	#
	def __init__(self):
		Thread.__init__(self)
		self.observers = []

	##
	# Register a certaain observer to observer the progress of the command
	# @param self the instance pointer
	# @param observer TiseanViewObserver instance
	#	
	def register_observer(self,observer):
		self.observers.append(observer)

	##
	# Starts the execution of a command
	# @param self the instance pointer
	# @param command string with full path of the command to be executed
	#		
	def execute_command(self,command):
		self.command = command
		self.start()
	
	##
	# Creates a subprocess of the command and opens a pipe to trace it
	# @param self the instance pointer
	# @param command string with full path of the command to be executed
	#	
	def get_popen(self,command):
	     sp = subprocess
	     return subprocess.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT)

	##
	# Reads lines from a file descriptor, uses to prevent problems of no content sent to the output 
	# when reading from the pipe
	# @param self the instance pointer
	#	
	def readlines(self,fd):
	    while 1:
			line = fd.readline()
			if not line:
				break
			yield line

	##
	# Send a certain message to all the observers that have been registered
	# when reading from the pipe
	# @param self the instance pointer
	# @param message the message to send to the observers
	#	
	def notify_observers(self,message):
		for observer in self.observers:
			observer.set_update(message)
			time.sleep(0.001)

	##
	# Implementation of the execution of the command and update of the observers
	# @param self the instance pointer
	#		
	def run(self):
		command = self.command
		self.notify_observers('**** Execution Started ****\n' + 'command called: ' + self.command + "\n**************************\n")

		popen = self.get_popen(command.split())
		while True:
			for line in self.readlines(popen.stdout):
				self.notify_observers(line)
			if popen.poll() != None: break
		
		self.notify_observers('** Execution Finished **')