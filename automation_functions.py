import webbrowser
import os
import psutil
from PIL import ImageGrab
import subprocess

def open_chrome():
    """Opens the Google Chrome web browser."""
    webbrowser.open("https://www.google.com")
    return "Chrome opened successfully"

def open_calculator():
    """Opens the Windows calculator application."""
    import subprocess
    try:
        subprocess.Popen('calc.exe')
        return "Calculator opened successfully"
    except Exception as e:
        return f"Error opening calculator: {str(e)}"

def open_notepad():
    """Starts the Notepad text editor."""
    os.system("notepad")  # Windows-specific
    return "Notepad opened successfully"

def get_cpu_usage():
    """Retrieves the current CPU usage percentage."""
    return f"Current CPU usage: {psutil.cpu_percent(interval=1)}%"

def get_ram_usage():
    """Gets the current RAM usage percentage."""
    return f"Current RAM usage: {psutil.virtual_memory().percent}%"

def take_screenshot():
    """Takes a screenshot and saves it to the desktop."""
    screenshot = ImageGrab.grab()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    screenshot_path = os.path.join(desktop_path, "screenshot.png")
    screenshot.save(screenshot_path)
    return f"Screenshot saved to {screenshot_path}"

def list_running_processes():
    """Lists the top 5 processes by memory usage."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        processes.append(proc.info)
    
    top_processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:5]
    return "\n".join([f"{p['name']} (PID: {p['pid']}): {p['memory_percent']:.2f}%" for p in top_processes])

def check_internet_connection():
    """Checks if the internet connection is working."""
    try:
        subprocess.check_output(["ping", "-n", "1", "8.8.8.8"], stderr=subprocess.STDOUT, universal_newlines=True)
        return "Internet connection is working"
    except subprocess.CalledProcessError:
        return "No internet connection"