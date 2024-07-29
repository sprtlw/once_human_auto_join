Auto-Join Full Server Script for ONCE_HUMAN
This Python script provides an automated method of joining a full server on ONCE_HUMAN.

Automatically finds and clicks the "No Hover" button
Detects the "Back" button and presses 'ESC'
Runs for a maximum of 30 iterations of not finding matching images, or until the 'q' key is pressed
Works specifically with the ONCE_HUMAN game window

Prerequisites
Before running this script, make sure you have Python installed on your system. This script has been tested with Python 3.7+.
Installation

Clone this repository or download the script files.
Navigate to the project directory.
Install the required libraries using the requirements.txt file:
Copypip install -r requirements.txt
This will install the following packages:

pyautogui
pygetwindow
keyboard



Usage

Ensure you have the required image files in the same directory as the script:

no_hover.png: An image of the "No Hover" button
back.png: An image of the "Back" button


Run the script:
Copypython script_name.py

The script will automatically activate the ONCE_HUMAN game window and start the clicking process.
To stop the script before it completes 30 iterations, press the 'q' key.
After the script finishes, press Enter/Return to exit.

How it Works

The script activates the ONCE_HUMAN game window.
It starts a separate thread to check for the 'q' key press.
In the main loop:

It searches for the "No Hover" button and clicks it when found.
It then looks for the "Back" button and presses 'ESC' when found.
This process repeats until either 30 iterations are completed or the 'q' key is pressed.



Customization
You can modify the following variables in the main() function to customize the script:

no_hover: Filename of the "No Hover" button image
back: Filename of the "Back" button image
window_title: Title of the game window

Troubleshooting
If you encounter any issues:

Ensure all required libraries are correctly installed.
Check that the image files (no_hover.png and back.png) are in the same directory as the script and match the in-game elements.
Verify that the ONCE_HUMAN game window is open and visible before running the script.

Disclaimer
This script is intended for educational purposes only. Make sure you comply with the game's terms of service when using automated scripts.
License
MIT License
