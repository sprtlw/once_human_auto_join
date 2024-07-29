# Auto-Join Full Server Script for ONCE_HUMAN

This Python script provides an automated method of joining a full server on ONCE_HUMAN. It uses image recognition to locate specific elements on the screen and perform actions accordingly.

## Features

- Automatically finds and clicks the "No Hover" button
- Detects the "Back" button and presses 'ESC'
- Runs for a maximum of 30 iterations or until the 'q' key is pressed
- Works specifically with the ONCE_HUMAN game window

## Prerequisites

Before running this script, make sure you have Python installed on your system. This script has been tested with Python 3.7+.

## Installation

1. Clone this repository or download the script files.

2. Navigate to the project directory.

3. Install the required libraries using the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

   This will install the following packages:
   - pyautogui
   - pygetwindow
   - keyboard

## Usage

1. Ensure you are on the main screen of ONCE_HUMAN, and have the required image files in the same directory as the script:
   - `no_hover.png`: An image of the "No Hover" button
   - `back.png`: An image of the "Back" button

2. Run the script:

   ```
   python script_name.py
   ```

3. The script will automatically activate the ONCE_HUMAN game window and start the clicking process.

4. To stop the script before it completes 30 iterations, press the 'q' key.

5. After the script finishes, press Enter/Return to exit.

## How it Works

1. The script activates the ONCE_HUMAN game window.
2. It starts a separate thread to check for the 'q' key press.
3. In the main loop:
   - It searches for the "No Hover" button and clicks it when found.
   - It then looks for the "Back" button and presses 'ESC' when found.
   - This process repeats until either 30 iterations are completed or the 'q' key is pressed.

## Customization

You can modify the following variables in the `main()` function to customize the script:

- `no_hover`: Filename of the "No Hover" button image
- `back`: Filename of the "Back" button image
- `window_title`: Title of the game window

## Troubleshooting

If you encounter any issues:

1. Ensure all required libraries are correctly installed.
2. Check that the image files (`no_hover.png` and `back.png`) are in the same directory as the script and match the in-game elements.
3. Verify that the ONCE_HUMAN game window is open and visible before running the script.

## Disclaimer

This script is intended for educational purposes only. Make sure you comply with the game's terms of service when using automated scripts.

## License

[MIT License](https://opensource.org/licenses/MIT)
