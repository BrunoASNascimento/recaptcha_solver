import pyautogui


def click_fig_center(img_name, confidence=0.9):
    print(f'[INFO] Read image: {img_name}')

    button_location = pyautogui.locateOnScreen(
        img_name,
        confidence=confidence,
        grayscale=True
    )
    center_point = pyautogui.center(button_location)
    x_point, y_point = center_point
    pyautogui.click(x_point, y_point)

    return
