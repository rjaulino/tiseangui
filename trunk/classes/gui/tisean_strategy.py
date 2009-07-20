from tisean_widgets import TiseanTextParameterWidget
from tisean_widgets import TiseanOptionsParameterWidget
from tisean_widgets import TiseanFileWidget
from tisean_widgets import TiseanSimpleParameterWidget

##
# Development Documentation for the TiseanGuiParameterBuildStrategy class.
# Base interface that defines a Build Strategy
# 
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanGuiParameterBuildStrategy:

	##
	# The Constructor
	# 
	# @param self The instance pointer
	#
	def __init__(self):
		pass

	##
	# Builds the widget
	#
	# @param self The instance pointer
	#
	def build_widget(self):
		pass		

##
# Development Documentation for the TiseanGuiTextParameterBuildStrategy class.
# Strategy that builds a Text Parameter Widget.
#
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanGuiTextParameterBuildStrategy(TiseanGuiParameterBuildStrategy):
	
	##
	# The Constructor
	# 
	# @param self The instance pointer
	#	
	def __init__(self):
		TiseanGuiParameterBuildStrategy.__init__(self)

	##
	# Builds the widget
	#
	# @param self The instance pointer
	#
	def build_widget(self,parameterConfig):
		widget = TiseanTextParameterWidget(parameterConfig.get_value(),parameterConfig.get_name())
		if (parameterConfig.is_required()):
			widget.set_required()
		return widget

##
# Development Documentation for the TiseanController class.
# Strategy that builds a Options Parameter Widget.
# 
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanGuiOptionsParameterBuildStrategy(TiseanGuiParameterBuildStrategy):
	
	##
	# The Constructor
	# 
	# @param self The instance pointer
	#
	def __init__(self):
		TiseanGuiParameterBuildStrategy.__init__(self)

	##
	# Builds the widget
	#
	# @param self The instance pointer
	#
	def build_widget(self,parameterConfig):

		options = parameterConfig.get_options()
		widget = TiseanOptionsParameterWidget(parameterConfig.get_value(),parameterConfig.get_name(),options)
		if (parameterConfig.is_required()):
			widget.set_required()
		return widget

##
# Development Documentation for the TiseanController class.
# Strategy that builds a File Parameter Widget.
# 
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanGuiFileParameterBuildStrategy(TiseanGuiParameterBuildStrategy):

	##
	# The Constructor
	# 
	# @param self The instance pointer
	#
	def __init__(self):
		TiseanGuiParameterBuildStrategy.__init__(self)

	##
	# Builds the widget
	#
	# @param self The instance pointer
	#
	def build_widget(self,parameterConfig):
		
		widget = TiseanFileWidget(parameterConfig.get_value(),parameterConfig.get_name())
		if (parameterConfig.is_required()):
			widget.set_required()
		return widget

##
# Development Documentation for the TiseanController class.
# Strategy that builds a Simple Parameter Widget.
# 
# @author Martin Ramos Mejia
# @version 0.1
#
class TiseanGuiSimpleParameterBuildStrategy(TiseanGuiParameterBuildStrategy):

	##
	# The Constructor
	# 
	# @param self The instance pointer
	#
	def __init__(self):
		TiseanGuiParameterBuildStrategy.__init__(self)

	##
	# Builds the widget
	#
	# @param self The instance pointer
	#
	def build_widget(self,parameterConfig):
		widget = TiseanSimpleParameterWidget(parameterConfig.get_value(),parameterConfig.get_name())
		if (parameterConfig.is_required()):
			widget.set_required()
		return widget