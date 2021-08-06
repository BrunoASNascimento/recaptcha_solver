import os
import pyautogui
from .human_style import human_digite, time_by_img
from .click_img import click_fig_left, click_fig_center
import pydub
import speech_recognition as sr


__all__ = ['recaptcha_solver']


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


def test_limit_recaptcha(img_error_recaptcha):
    test_error = False
    while test_error == True:
        test_error = time_by_img(
            img_error_recaptcha, 1)
        if test_error == True:
            print('[ERROR] Limit recaptcha.')
            print('[BREAK CODE]')
            break


def recaptcha_solver(path_download: str,  img_activate_recaptcha: str,
                     img_sound: str, img_reset_recaptcha: str, img_download_recaptcha: str, img_error_recaptcha: str,
                     img_options_sound: str, img_download_sound: str, img_close_sound: str, imgs_text_box: list,
                     imgs_verify: list, img_check: str, img_back_page: str = None, number_try: int = 5) -> bool:

    pyautogui.moveTo(10, 10)
    pass_test = False
    control = 0

    while (pass_test == False) and (control <= number_try):
        control += 1
        print('[INFO] Try to break the recaptcha.')

        # time_by_img(img_init_page)
        # click_fig_center(img_init_page)

        recaptcha_init = time_by_img(img_activate_recaptcha, 3)
        if recaptcha_init == True:
            click_fig_center(img_activate_recaptcha)
        test_limit_recaptcha(img_error_recaptcha)

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

        pass_test = time_by_img(
            img_check,
            5
        )
        if pass_test == False:
            try:
                time_by_img(img_download_recaptcha)
                click_fig_center(img_download_recaptcha)

                test_limit_recaptcha(img_error_recaptcha)

                time_by_img(img_options_sound)
                click_fig_left(img_options_sound)

                time_by_img(img_download_sound)
                click_fig_center(img_download_sound)

                time_by_img(img_close_sound)
                click_fig_left(img_close_sound)

                for img_text_box in imgs_text_box:
                    try:
                        time_by_img(img_text_box, 2)
                        click_fig_center(img_text_box)
                    except Exception as error:
                        print(f'[ERROR] {img_text_box} - {error}')

                phrase_regognize = get_text_by_audio(dirpath)
                print(f'[INFO] Recognize: {phrase_regognize}')

                if phrase_regognize != None:
                    human_digite(phrase_regognize)

                    for img_verify in imgs_verify:
                        try:
                            time_by_img(img_verify, 2)
                            click_fig_center(img_verify)

                        except Exception as error:
                            print(f'[ERROR] {img_verify} - {error}')

                pass_test = time_by_img(
                    img_check,
                    5
                )

            except Exception as error:
                print(f'[ERROR] Error in Recaptcha: {error}')
                if img_back_page != None:
                    if time_by_img(img_back_page) == True:
                        click_fig_center(img_back_page)

        if os.path.exists(dirpath):
            os.remove(dirpath)

    return pass_test
