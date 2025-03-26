import inspect
from utils.logger import logger

class CustomFunctionManager:
    def __init__(self):
        self.custom_functions = {}
    
    def register_function(self, func_name, func_code, description):
        """Register a new custom function."""
        try:
            # Create function namespace
            namespace = {}
            
            # Execute the function code in the namespace
            exec(func_code, namespace)
            
            # Get the function object
            if func_name in namespace:
                func = namespace[func_name]
                
                # Add docstring
                func.__doc__ = description
                
                # Store the function
                self.custom_functions[func_name] = func
                logger.info(f"Successfully registered custom function: {func_name}")
                return True
            else:
                logger.error(f"Function {func_name} not found in provided code")
                return False
                
        except Exception as e:
            logger.error(f"Error registering function {func_name}: {str(e)}")
            return False
    
    def get_function(self, func_name):
        """Retrieve a custom function by name."""
        return self.custom_functions.get(func_name)
    
    def list_functions(self):
        """List all registered custom functions."""
        return {
            name: {
                'description': func.__doc__,
                'signature': str(inspect.signature(func))
            }
            for name, func in self.custom_functions.items()
        }