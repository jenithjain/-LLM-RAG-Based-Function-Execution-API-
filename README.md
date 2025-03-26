# -LLM-RAG-Based-Function-Execution-API-
# Automation Assistant
A natural language-powered automation tool that helps users perform system tasks through simple text commands.

## Overview

Automation Assistant is a Python-based application that uses Retrieval-Augmented Generation (RAG) to match user queries with appropriate automation functions. It provides both a web interface (Streamlit) and an API (FastAPI) for executing common system tasks.

## Testpoint Screenshots
![Screenshot 2025-03-26 185614](https://github.com/user-attachments/assets/b0603219-924e-4877-9159-befe365e9d7f)

![Screenshot 2025-03-26 191003](https://github.com/user-attachments/assets/af4f84da-ee05-4310-8525-bab654b20443)

![Screenshot 2025-03-26 191425](https://github.com/user-attachments/assets/e3e47e12-4a5f-4199-bcfe-a572f31aad59)

![Screenshot 2025-03-26 191158](https://github.com/user-attachments/assets/f1b55896-cc20-495a-8069-531b409cc1a7)

![Screenshot 2025-03-26 191126](https://github.com/user-attachments/assets/c31593f4-f199-46c0-aedb-112b085d0811)

## Demo Video



https://github.com/user-attachments/assets/a6c89531-6ac2-4614-a804-707472d77615

## Features

- **Natural Language Processing**: Describe tasks in plain English
- **Multiple Interfaces**: Web UI and REST API
- **System Automation**: Execute common Windows tasks
- **Code Generation**: Get executable Python code for each function
- **Custom Functions**: Register and use your own automation functions

## Available Functions

- Open applications (Chrome, Calculator, Notepad)
- System monitoring (CPU usage, RAM usage)
- Take screenshots
- List running processes
- Check internet connectivity


## Bonus Features
-Advanced Logging System: Rotating file logs with console output
-Error Handling Framework: Custom exception classes and decorators
-Input Validation: Query and function validation utilities
-Custom Function Registration: Dynamic function creation and management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/automation-assistant.git
   cd automation-assistant

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables (if needed)

## Usage

### Web Interface
```bash
streamlit run app.py
```
Then open your browser to http://localhost:8501

### API
```bash
uvicorn api:app --reload
```
API Documentation available at http://localhost:8000/docs

**Example API Request:**
```bash
curl -X POST "http://localhost:8000/execute" \
     -H "Content-Type: application/json" \
     -d '{"query": "Check my CPU usage"}'
```

**Response:**
```json
{
  "result": "Current CPU usage: 23%",
  "code": "import psutil\npsutil.cpu_percent(interval=1)",
  "status": "success"
}
```

## Project Structure
```bash
automation-assistant/
├── app.py            # Streamlit web interface
├── api.py            # FastAPI endpoints
├── config.py         # Configuration settings
├── functions/        # Automation function modules
├── utils/            # Helper functions and utilities
├── requirements.txt  # Dependency list
└── README.md         # Documentation
```

Requirements
Python 3.8+

Windows OS (for system-specific functions)

Dependencies listed in requirements.txt
