import os

##
# 
#
#
class TiseanRunner():

	def __init__(self):
		self.observers = []
	
	def register_observer(self,observer):
		self.observers.append(observer)
	
	def execute_command(self,command):
		self.command = command
		return self.run()
	
	def run(self):
		
		fin, fout = os.popen4('bin/./' + self.command)

		for line in fout.readlines():		
			for observer in self.observers:
				observer.set_update(line)
		
		fin.close()
		fout.close()
		
