from tisean_widgets import TiseanCommandForm
from tisean_widgets import TiseanFileDialogWidget
from tisean_widgets import TiseanFileWidget
from tisean_config import TiseanCommandConfig

##
# Development Documentation for the TiseanGuiFactory class.
# Represents a factory that build the dinamics aspects of the GUI given certain TiseanCommandConfig.
# 
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanGuiFactory:

	##
	# The Constructor
	#
	# @param self the instance pointer
	#
	def __init__(self):
		pass
	
	##
	# Builds a Form given a certain TiseanCommandConfig
	#
	# @param self the instance pointer
	# @param tiseanCommandConfig a TiseanCommandConfig instance
	# @param controller a TiseanController instance to be linked with the form
	# 
	def create_form(self,tiseanCommandConfig,controller): 
	
		#Input and Output Widgets
		if (tiseanCommandConfig.has_input()):
			inputWidget = TiseanFileWidget('','Input Filename')
			inputWidget.set_required()
		
		outputWidget = TiseanFileWidget('-o','Output Filename')
		
		parameters = tiseanCommandConfig.get_parameters()
		parameterWidgets = []

		if (tiseanCommandConfig.has_input()):
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
	# Creates a widget for a certain parameter configuration
	#
	# @param self The instance pointer
	# @param parameterConfig The TiseanParameterConfig in which the widget will be based.
	def create_parameter_widget(self,parameterConfig):
	
		strategy = parameterConfig.get_build_strategy()
		widget = strategy.build_widget(parameterConfig)
		return widget
