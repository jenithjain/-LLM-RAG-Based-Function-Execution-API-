import streamlit as st
import os
import importlib
import nest_asyncio
from rag_retrieval import FunctionRetriever
from code_generator import generate_code

# Apply nest_asyncio to fix event loop issues
nest_asyncio.apply()

# Set page configuration
st.set_page_config(
    page_title="Automation Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize the function retriever
@st.cache_resource
def load_retriever():
    return FunctionRetriever()

retriever = load_retriever()

# App title and description
st.title("🤖 Automation Assistant")
st.markdown("""
This application helps you automate tasks using natural language commands.
Simply describe what you want to do, and the system will find the appropriate function and execute it.
""")

# User input
user_query = st.text_input("What would you like to do?", placeholder="e.g., Open calculator, Check CPU usage, Take a screenshot")

if user_query:
    matches = retriever.retrieve_function(user_query)
    
    if matches:
        st.subheader("Found matching function:")
        match = matches[0]  # Get the best match only
        
        st.markdown(f"**Function:** {match['function_name']}")
        st.markdown(f"**Description:** {match['description']}")
        
        # Show generated code
        with st.expander("View Generated Code"):
            generated_code = generate_code(match['function_name'])
            st.code(generated_code, language="python")
            
            # Download button for the generated code
            st.download_button(
                label="Download Python Script",
                data=generated_code,
                file_name=f"{match['function_name']}_script.py",
                mime="text/plain"
            )
        
        # Execute function button
        if st.button("Execute Function"):
            st.info(f"Executing {match['function_name']}...")
            
            try:
                module = importlib.import_module("automation_functions")
                func = getattr(module, match['function_name'])
                result = func()
                
                st.success("Function executed successfully!")
                if result:
                    st.write("Result:")
                    st.markdown(f"```\n{result}\n```")
            except Exception as e:
                st.error(f"Error executing function: {str(e)}")
    else:
        st.warning("No matching functions found. Please try a different query.")

# Display available functions
with st.sidebar:
    st.subheader("Available Automation Functions")
    for name, description in retriever.functions.items():
        with st.expander(name):
            st.write(description)