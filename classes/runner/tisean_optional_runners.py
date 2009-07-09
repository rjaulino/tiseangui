import sys
import os
import time
import subprocess
import tempfile
from subprocess import Popen,PIPE
from threading import Thread
#
class TiseanRunner(Thread):

	def __init__(self):
		Thread.__init__(self)
		self.observers = []
	
	def register_observer(self,observer):
		self.observers.append(observer)
	
	def execute_command(self,command):
		self.command = command
		self.start()
	
	def get_popen(self,command):
	     sp = subprocess
	     return subprocess.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT)

	def readlines(self,fd):
	    while 1:
			print('corre')
			line = fd.readline()
			if not line:
				break
			yield line	
	
	def run(self):
		
#subprocess option - asynchronic
		
#		pipe = Popen(['/media/psf/Home/Work/Personal/Proyects/tiseangui/bin/'+self.command,'-h'], shell=True, bufsize=100, stdout=PIPE)
#		pipe = Popen(['/media/psf/Home/Work/Personal/Proyects/tiseangui/bin/arima-model','-h'], stdout=subprocess.PIPE)
# 		pipe = Popen(['/usr/bin/gcc'],stdout=PIPE)

#		pipe = Popen('cat --help', shell=True, bufsize=1, stdout=subprocess.PIPE)
#		pipe = Popen('ping -c 10 localhost', shell=True, bufsize=1, stdout=subprocess.PIPE)
#		pipe = Popen('ls -l', shell=True, bufsize=1, stdout=subprocess.PIPE)
#		pipe = Popen('/usr/games/fortune', shell=True, bufsize=1, stdout=subprocess.PIPE)
#		pipe = Popen('dmesg', shell=True, bufsize=1, stdout=subprocess.PIPE)
#		output = pipe.stdout

		# we open a pipe to read the execution of the command
#		while True:
#			strBuffer = pipe.communicate()[0]
#			# we update all the observer with each line of the strBuffer
#			lines = strBuffer.split("\n")
#			for line in lines:
#				print('runner:  ' + line)
#				for observer in self.observers:
#					observer.set_update(line)
#				time.sleep(0.5)
#			if strBuffer == '' and pipe.poll() != None: break


#os option - asynchronic
#		output = os.popen('/media/psf/Home/Work/Personal/Proyects/tiseangui/bin/arima-model -h','r');
#		output = os.popen('fortune','r');

#		while True:
#			line = output.readline()
#			print('runner:  ' + line)
#			for observer in self.observers:
#				observer.set_update(line)
#			time.sleep(0.1)
#			if line == '' : break

#example - from miya 
#		command = '/media/psf/Home/Work/Personal/Proyects/tiseangui/bin/arima-model'
#		command = '/usr/bin/gcc -v'
#		command = 'ping -c 5 localhost'
		command = self.command
		popen = self.get_popen(command.split())
		while True:
			for line in self.readlines(popen.stdout):
				for observer in self.observers:
					observer.set_update(line)
				time.sleep(0.01)
			if popen.poll() != None: break