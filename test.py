from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import getpass

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

path_download = f"C:/Users/{getpass.getuser()}/Downloads"

img_activate_recaptcha = 'img/img_activate_recaptcha.png'
img_sound = 'img/img_sound.png'
img_reset_recaptcha = 'img/img_reset_recaptcha.png'
img_download_recaptcha = 'img/img_download_recaptcha.png'
img_error_recaptcha = 'img/img_error_recaptcha.png'
img_options_sound = 'img/img_options_sound.png'
img_download_sound = 'img/img_download_sound.png'
img_close_sound = 'img/img_close_sound.png'
imgs_text_box = ['img/imgs_text_box_001.png',
                 'img/imgs_text_box_002.png']
imgs_verify = ['img/imgs_verify_001.png',
               'img/imgs_verify_002.png']
img_check = 'img/img_check.png'

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
