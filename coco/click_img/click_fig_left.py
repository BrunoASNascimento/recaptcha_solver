import pyautogui

__all__ = ['click_fig_left']


def click_fig_left(img_name, confidence=0.9):
    print(f'[INFO] Read image: {img_name}')

    button_location = pyautogui.locateOnScreen(
        img_name,
        confidence=confidence,
        grayscale=True
    )
    left, _, width, _ = button_location
    center_point = pyautogui.center(button_location)
    _, y_point = center_point
    pyautogui.click((left+width-2), y_point)

    return
