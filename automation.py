import datetime
import os
import subprocess
import platform

def get_system_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def open_application(app_name: str):
    try:
        system = platform.system()

        if system == "Windows":
            subprocess.Popen(app_name)
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", app_name])
        else:  # Linux
            subprocess.Popen([app_name])

        print(f"Opening {app_name}...")

    except Exception as e:
        print(f"Failed to open application: {e}")
