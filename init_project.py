import os
import sys
from utils.logger import logger

def init_project():
    """Initialize project structure and verify dependencies"""
    try:
        # Create necessary directories
        directories = [
            "e:\\InterLLM\\automation_assistant\\logs",
            "e:\\InterLLM\\automation_assistant\\utils",
            "e:\\InterLLM\\automation_assistant\\data"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            logger.info(f"Created directory: {directory}")
        
        # Verify required files exist
        required_files = [
            "automation_functions.py",
            "rag_retrieval.py",
            "custom_functions.py",
            "utils/__init__.py",
            "utils/logger.py",
            "utils/error_handler.py",
            "utils/validation.py"
        ]
        
        base_path = "e:\\InterLLM\\automation_assistant"
        missing_files = []
        
        for file in required_files:
            file_path = os.path.join(base_path, file)
            if not os.path.exists(file_path):
                missing_files.append(file)
        
        if missing_files:
            logger.error(f"Missing required files: {', '.join(missing_files)}")
            return False
        
        logger.info("Project initialization completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"Project initialization failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = init_project()
    sys.exit(0 if success else 1)