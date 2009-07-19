from tisean_widgets import TiseanTextParameterWidget
from tisean_widgets import TiseanOptionsParameterWidget
from tisean_widgets import TiseanFileWidget
from tisean_widgets import TiseanSimpleParameterWidget

class TiseanGuiParameterBuildStrategy:

	def __init__(self):
		pass

	def build_widget(self):
		pass		

class TiseanGuiTextParameterBuildStrategy(TiseanGuiParameterBuildStrategy):
	
	def __init__(self):
		TiseanGuiParameterBuildStrategy.__init__(self)

	def build_widget(self,parameterConfig):
		widget = TiseanTextParameterWidget(parameterConfig.get_value(),parameterConfig.get_name())
		if (parameterConfig.is_required()):
			widget.set_required()
		return widget


class TiseanGuiOptionsParameterBuildStrategy(TiseanGuiParameterBuildStrategy):
	
	def __init__(self):
		TiseanGuiParameterBuildStrategy.__init__(self)

	def build_widget(self,parameterConfig):

		options = parameterConfig.get_options()
		widget = TiseanOptionsParameterWidget(parameterConfig.get_value(),parameterConfig.get_name(),options)
		if (parameterConfig.is_required()):
			widget.set_required()
		return widget

class TiseanGuiFileParameterBuildStrategy(TiseanGuiParameterBuildStrategy):

	def __init__(self):
		TiseanGuiParameterBuildStrategy.__init__(self)

	def build_widget(self,parameterConfig):
		
		widget = TiseanFileWidget(parameterConfig.get_value(),parameterConfig.get_name())
		if (parameterConfig.is_required()):
			widget.set_required()
		return widget

class TiseanGuiSimpleParameterBuildStrategy(TiseanGuiParameterBuildStrategy):

	def __init__(self):
		TiseanGuiParameterBuildStrategy.__init__(self)

	def build_widget(self,parameterConfig):
		widget = TiseanSimpleParameterWidget(parameterConfig.get_value(),parameterConfig.get_name())
		if (parameterConfig.is_required()):
			widget.set_required()
		return widget