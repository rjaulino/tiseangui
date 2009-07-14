import os
import time
import gobject
from threading import Thread
from threading import Lock

##
# 
#
#
class TiseanViewSimpleUpdater():

	def __init__(self,console):

		self.console = console
		self.message = ''
	
	def set_update(self,message):
		self.message = message
		scrolledWindow = self.console.get_child()
		textConsole = scrolledWindow.get_child()
		textBuffer = textConsole.get_buffer()
		startIter = textBuffer.get_iter_at_line_offset(0, 0)
		endIter = textBuffer.get_iter_at_line_offset(textBuffer.get_line_count()-1,0)
		text = textBuffer.get_text(startIter,endIter)
		textBuffer.set_text(text + message)

##
# 
#
#
class TiseanViewUpdater(Thread):

	def __init__(self,console):
		Thread.__init__(self)
		self.console = console
		self.message = ''
		self.newMessage = False
		self.running = False
		self.lock = Lock()
	
	def set_update(self,message):
		self.lock.acquire()
		try:
			self.message = message
			self.newMessage = True
		finally:
			self.lock.release()
	
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

	def start_updater(self):
		self.lock.acquire()
		try:
			self.running = True
		finally:
			self.lock.release()

		self.start()
	
	def run(self):
		while (self.running is True):
			if (self.newMessage is True):
				self.update_message()
	
	def stop_updater(self):
		
		self.lock.acquire()
		try:
			self.running = False
		finally:
			self.lock.release()
		
		self.join()
