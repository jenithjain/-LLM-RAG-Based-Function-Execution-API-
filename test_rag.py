from rag_retrieval import FunctionRetriever
from custom_functions import CustomFunctionManager
from utils.logger import logger

def test_rag():
    # Initialize the retriever and custom function manager
    retriever = FunctionRetriever()
    custom_manager = CustomFunctionManager()
    
    # Register a custom function
    custom_func = """
def custom_greeting(name="World"):
    '''Creates a custom greeting message for the given name.'''
    return f"Hello, {name}!"
"""
    
    custom_manager.register_function(
        "custom_greeting",
        custom_func,
        "Creates a custom greeting message for the given name."
    )
    
    # Add custom function to RAG index
    retriever.update_index(
        "custom_greeting",
        "Creates a custom greeting message for the given name."
    )
    
    # Test queries
    test_queries = [
        "Check system CPU usage",
        "Take a screenshot of my screen",
        "Show running processes",
        "Open calculator app",
        "Create a greeting message"
    ]
    
    # Test retrieval for each query
    for query in test_queries:
        logger.info(f"Testing query: {query}")
        matches = retriever.retrieve_function(query)
        
        print(f"\nQuery: {query}")
        print("Matching functions:")
        for match in matches:
            print(f"- {match['function_name']}")
            print(f"  Description: {match['description']}")
            
            # Execute the function
            try:
                if match['function_name'] in custom_manager.custom_functions:
                    func = custom_manager.get_function(match['function_name'])
                else:
                    module = __import__('automation_functions')
                    func = getattr(module, match['function_name'])
                
                result = func()
                print(f"  Result: {result}")
            except Exception as e:
                logger.error(f"Error executing {match['function_name']}: {str(e)}")

if __name__ == "__main__":
    test_rag()