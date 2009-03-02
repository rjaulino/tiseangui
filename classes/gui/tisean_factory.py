from tisean_widgets import TiseanCommandForm
from tisean_widgets import TiseanFileDialogWidget
from tisean_widgets import TiseanFileWidget
from tisean_config import TiseanCommandConfig

class TiseanGuiFactory:

	def __init__(self):
		pass
	
	
	def create_form(self,tiseanCommandConfig,controller): 
	
		#Input and Output Widgets
		inputWidget = TiseanFileWidget('input','Input Filename: ')
		outputWidget = TiseanFileWidget('output','Output Filename: ')
		
		parameters = tiseanCommandConfig.get_parameters()
		parameterWidgets = []
		parameterWidgets.append(inputWidget)
		parameterWidgets.append(outputWidget)

		for key in parameters:
			#we get every parameter configuration
			parameterConfig = parameters[key]
			widget = self.create_parameter_widget(parameterConfig)
			parameterWidgets.append(widget)
		
		form = TiseanCommandForm(tiseanCommandConfig.get_name(),parameterWidgets,controller)

		return form
	
	##
	#
	#
	#
	#
	def create_parameter_widget(self,parameterConfig):
	
		strategy = parameterConfig.get_build_strategy()
		widget = strategy.build_widget(parameterConfig)
		return widget
