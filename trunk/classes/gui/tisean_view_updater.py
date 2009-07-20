import os
import time
import gobject
from threading import Thread
from threading import Lock


##
# Development Documentation for the TiseanViewUpdater class.
# Thread that performs the update of the view when it gets a notification from the running thread. 
# 
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanViewUpdater(Thread):

	##
	# The Constructor
	#
	# @param self The instance pointer
	# @param console Console Widget Instance where the update it's going to be done 
	#
	def __init__(self,console):
		Thread.__init__(self)
		self.console = console
		self.message = ''
		self.newMessage = False
		self.running = False
		self.lock = Lock()
	
	##
	# Notification of the updater of a new message
	#
	# @param self The instance pointer
	# @param message New message to be processed by the updater
	#
	def set_update(self,message):
		self.lock.acquire()
		try:
			self.message = message
			self.newMessage = True
		finally:
			self.lock.release()
	
	##
	# Sets the new message to console 
	#
	# @param self The instance pointer
	#
	def update_message(self):
		self.lock.acquire()
		try:
			scrolledWindow = self.console.get_child()
			textConsole = scrolledWindow.get_child()
			textBuffer = textConsole.get_buffer()
			endIter = textBuffer.get_end_iter()
			textBuffer.insert(endIter,"" + self.message)
			endIter = textBuffer.get_end_iter()
			textConsole.scroll_to_iter(endIter,0.2)
			self.newMessage = False
		finally:
			self.lock.release()

	##
	# Inits the updating Thread
	# 
	# @param self The instance pointer
	#
	def start_updater(self):
		self.lock.acquire()
		try:
			self.running = True
		finally:
			self.lock.release()

		self.start()
	
	
	##
	# Definition of the updating process of the Thread
	# 
	# @param self The instance pointer
	#
	def run(self):
		while (self.running is True):
			if (self.newMessage is True):
				self.update_message()
	
	##
	# Stops the updates process
	#
	# @param self The instance pointer
	#
	def stop_updater(self):
		
		self.lock.acquire()
		try:
			self.running = False
		finally:
			self.lock.release()
		
		self.join()
