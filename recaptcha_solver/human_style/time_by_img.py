import pyautogui
import time

__all__ = ['time_by_img']


def time_by_img(PATH_IMG, timeout_value=5):
    control_img = None
    control_timeout = 0
    while (control_img is None) and (control_timeout <= timeout_value):
        start_time = time.time()
        control_img = pyautogui.locateOnScreen(
            PATH_IMG,
            confidence=0.9,
            grayscale=True)
        control_timeout += (time.time()-start_time)
    if control_img is not None:
        return True
    else:
        print('[INFO] Timeout, image not found.')
        return False
