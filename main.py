from time import sleep

import threading as tg

import pyautogui as pag
import pygetwindow as gw
import keyboard as kb


def find_no_hover(no_hover=None):
    try:
        location = pag.locateOnScreen(no_hover, confidence=0.5)
    except pag.ImageNotFoundException:
        location = None

    if location:
        print(f"{no_hover} found at: {location}")

        pag.moveTo(location[0] + 100, location[1] + 20)
        pag.click()

        return True

    print(f"{no_hover} not found on screen.")

    return False


def find_back(back=None):
    try:
        location = pag.locateOnScreen(back, confidence=0.8)
    except pag.ImageNotFoundException:
        location = None

    if location:
        print(f"{back} found at: {location}")
        pag.press('esc')

        return True

    print(f"{back} not found on screen.")

    return False


def check_keypress():
    while True:
        if kb.is_pressed('q'):
            break

        sleep(0.1)


def main():
    no_hover = 'no_hover.png'
    back = 'back.png'

    window_title = 'ONCE_HUMAN'
    window = gw.getWindowsWithTitle(window_title)[0]
    window.activate()

    keypress_thread = tg.Thread(target=check_keypress, daemon=True)
    keypress_thread.start()

    while keypress_thread.is_alive():

        while find_no_hover(no_hover) is False:
            find_no_hover(no_hover)
            sleep(1)

        while find_back(back) is False:
            find_back(back)
            sleep(1)

    print()
    print("Finished.")
    print()
    input("Press Enter/Return to exit...")


if __name__ == "__main__":
    main()
