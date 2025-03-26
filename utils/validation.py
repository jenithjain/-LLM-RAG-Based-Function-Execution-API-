import inspect
from .logger import logger

def validate_function(func):
    """Validate that a function meets the required criteria"""
    if not callable(func):
        logger.error("Object is not callable")
        return False
    
    if not func.__doc__:
        logger.warning(f"Function {func.__name__} lacks documentation")
        return False
    
    return True

def validate_query(query):
    """Validate user query"""
    if not isinstance(query, str):
        logger.error("Query must be a string")
        return False
    
    if not query.strip():
        logger.error("Query cannot be empty")
        return False
    
    return True