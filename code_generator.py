def generate_code(function_name):
    """Generate a Python script to invoke the given function."""
    code = f"""from automation_functions import {function_name}

def main():
    try:
        result = {function_name}()
        print("{function_name} executed successfully.")
        if result is not None:
            print(f"Result: {{result}}")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()"""
    return code.strip()

def generate_executable_code(function_name):
    """Generate a single line of code to execute the function directly."""
    return f"from automation_functions import {function_name}; result = {function_name}()"