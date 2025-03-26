from functools import wraps
from .logger import logger

class AutomationError(Exception):
    """Base exception class for automation errors"""
    pass

class FunctionExecutionError(AutomationError):
    """Raised when a function fails to execute"""
    pass

class RAGError(AutomationError):
    """Raised when RAG retrieval fails"""
    pass

def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            raise AutomationError(f"Operation failed: {str(e)}")
    return wrapper