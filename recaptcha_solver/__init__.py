import os
import pyautogui
from human_style import human_digite, time_by_img
from click_img import click_fig_left, click_fig_center
import pydub
import speech_recognition as sr

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


def get_text_by_audio(dirpath):
    phrase_regognize = None
    sound = pydub.AudioSegment.from_mp3(dirpath)
    sound.export(dirpath, format="wav")
    sample_audio = sr.AudioFile(dirpath)
    r = sr.Recognizer()

    with sample_audio as source:
        audio = r.record(source)
    phrase_regognize = r.recognize_google(audio, language='en-US')
    try:
        phrase_regognize = r.recognize_google(audio, language='en-US')
    except Exception as error:
        print(f'[ERROR] Recognize Google - {error}')

    return phrase_regognize


# print(get_text_by_audio(r'C:\Users\bruno\Downloads\audio (3).mp3'))


def test_limit_recaptcha(img_error_recaptcha):
    test_error = False
    while test_error == True:
        test_error = time_by_img(
            img_error_recaptcha, 1)
        if test_error == True:
            print('[ERROR] Limit recaptcha.')
            print('[BREAK CODE]')
            break


# img_init_page = ''
# img_activate_recaptcha = 'data\img\step_005.png'
# img_sound = 'data\img\step_006.png'
# img_reset_recaptcha = 'data\img\reset_recaptcha.png'
# img_download_recaptcha = 'data\img\step_007.png'
# img_error_recaptcha = 'data\img\step_recaptcha_erro.png'
# img_options_sound=img_options_sound
# img_download_sound=img_download_sound
# img_close_sound=img_close_sound
# imgs_text_box=['data/img/developer/step_011.png',
#  'data/img/developer/step_011-1.png']
# imgs_verify = ['data/img/developer/step_012.png',
            # 'data/img/developer/step_012-1.png']
# img_check = 'data/img/developer/step_recaptcha_ok.png'


def recaptcha_solver(img_back_page, path_download, img_init_page, img_activate_recaptcha, img_sound, img_reset_recaptcha, img_download_recaptcha, img_error_recaptcha, img_options_sound, img_download_sound, img_close_sound, imgs_text_box, imgs_verify, img_check):
    pyautogui.moveTo(10, 10)
    pass_test = False
    control = 0
    while (pass_test == False) and (control <= 10):
        control += 1
        print('[INFO] Try to break the recaptcha.')

        time_by_img(img_init_page)
        click_fig_center(img_init_page)

        recaptcha_init = time_by_img(img_activate_recaptcha, 3)
        if recaptcha_init == True:
            click_fig_center(img_activate_recaptcha)
        test_limit_recaptcha()

        dirpath = f'{path_download}/audio.mp3'

        if os.path.exists(dirpath):
            os.remove(dirpath)

        recaptcha_reset = time_by_img(img_reset_recaptcha, 1)
        if recaptcha_reset == True:
            click_fig_center(img_reset_recaptcha)

        audio_buttom = time_by_img(img_sound, 2)
        if audio_buttom == True:
            click_fig_center(img_sound)

        test_limit_recaptcha(img_error_recaptcha)

        try:
            time_by_img(img_download_recaptcha)
            click_fig_center(img_download_recaptcha)

            test_limit_recaptcha()

            time_by_img(img_options_sound)
            click_fig_left(img_options_sound)

            time_by_img(img_download_sound)
            click_fig_center(img_download_sound)

            time_by_img(img_close_sound)
            click_fig_left(img_close_sound)

            for step_011 in imgs_text_box:
                try:
                    time_by_img(step_011, 2)
                    click_fig_center(step_011)
                except Exception as error:
                    print(f'[ERROR] {step_011} - {error}')

            phrase_regognize = get_text_by_audio(dirpath)
            print(f'[INFO] Recognize: {phrase_regognize}')

            if phrase_regognize != None:
                human_digite(phrase_regognize)

                for step_012 in imgs_verify:
                    try:
                        time_by_img(step_012, 2)
                        click_fig_center(step_012)

                    except Exception as error:
                        print(f'[ERROR] {step_012} - {error}')

            pass_test = time_by_img(
                img_check,
                5
            )

        except Exception as error:
            print(f'[ERROR] Error in Recaptcha: {error}')
            time_by_img(img_back_page)
            click_fig_center(img_back_page)

        if os.path.exists(dirpath):
            os.remove(dirpath)

    return pass_test
