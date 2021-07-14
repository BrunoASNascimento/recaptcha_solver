from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from recaptcha_solver import recaptcha_solver


chrome_options = Options()
chrome_options.add_experimental_option(
    'debuggerAddress',
    'localhost:8989'
)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(
    executable_path='D:/developer/utils/tools/chrome_driver/windows/chromedriver_91.exe',
    options=chrome_options
)

driver.get('https://www.google.com/recaptcha/api2/demo')

path_download = "C:/Users/bruno/Downloads"

img_activate_recaptcha = 'D:/developer/github.com/projects/recaptcha_solver/data/img/step_005.png'
img_sound = 'D:/developer/github.com/projects/recaptcha_solver/data/img/step_006.png'
img_reset_recaptcha = 'D:/developer/github.com/projects/recaptcha_solver/data/img/reset_recaptcha.png'
img_download_recaptcha = 'D:/developer/github.com/projects/recaptcha_solver/data/img/step_007.png'
img_error_recaptcha = 'D:/developer/github.com/projects/recaptcha_solver/data/img/step_recaptcha_erro.png'
img_options_sound = 'D:/developer/github.com/projects/recaptcha_solver/data/img/step_008.png'
img_download_sound = 'D:/developer/github.com/projects/recaptcha_solver/data/img/step_009.png'
img_close_sound = 'D:/developer/github.com/projects/recaptcha_solver/data/img/step_010.png'
imgs_text_box = ['D:/developer/github.com/projects/recaptcha_solver/data/img/step_011.png',
                 'D:/developer/github.com/projects/recaptcha_solver/data/img/step_011-1.png']
imgs_verify = ['D:/developer/github.com/projects/recaptcha_solver/data/img/step_012.png',
               'D:/developer/github.com/projects/recaptcha_solver/data/img/step_012-1.png']
img_check = 'D:/developer/github.com/projects/recaptcha_solver/data/img/step_recaptcha_ok.png'

recaptcha_solver(
    path_download,
    img_activate_recaptcha,
    img_sound,
    img_reset_recaptcha,
    img_download_recaptcha,
    img_error_recaptcha,
    img_options_sound,
    img_download_sound,
    img_close_sound,
    imgs_text_box,
    imgs_verify,
    img_check
)
# driver.close()
