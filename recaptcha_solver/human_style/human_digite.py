import random
import pyautogui
import time

__all__ = ['human_digite']


def human_digite(str_value):
    for letter_user in str_value:
        interval_value = random.randrange(1_000, 1_300)/10_000
        pyautogui.write(letter_user)
        time.sleep(interval_value)
    return
