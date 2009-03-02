from tisean_widgets import TiseanIntegerParameterWidget
from tisean_widgets import TiseanOptionsParameterWidget

class TiseanGuiParameterBuildStrategy:

	def __init__(self):
		pass

	def build_widget(self):
		pass		

class TiseanGuiIntegerParameterBuildStrategy(TiseanGuiParameterBuildStrategy):
	
	def __init__(self):
		TiseanGuiParameterBuildStrategy.__init__(self)

	def build_widget(self,parameterConfig):
		return TiseanIntegerParameterWidget(parameterConfig.get_value(),parameterConfig.get_name())


class TiseanGuiOptionsParameterBuildStrategy(TiseanGuiParameterBuildStrategy):
	
	def __init__(self):
		TiseanGuiParameterBuildStrategy.__init__(self)

	def build_widget(self,parameterConfig):

		options = parameterConfig.get_options()
		return TiseanOptionsParameterWidget(parameterConfig.get_value(),parameterConfig.get_name(),options)

