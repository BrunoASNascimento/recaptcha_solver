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


def test_limit_recaptcha():
    test_error = False
    while test_error == True:
        test_error = time_by_img(
            'data/img/developer/step_recaptcha_erro.png', 1)
        if test_error == True:
            print('[ERROR] Limit recaptcha.')
            print('[BREAK CODE]')
            break


def recaptcha_solver(back_page):
    pyautogui.moveTo(10, 10)
    pass_test = False
    control = 0
    while (pass_test == False) and (control <= 10):
        control += 1
        print('[INFO] Try to break the recaptcha.')

        time_by_img('data/img/developer/click_title_page.png')
        click_fig_center('data/img/developer/click_title_page.png')

        recaptcha_init = time_by_img('data/img/developer/step_005.png', 3)
        if recaptcha_init == True:
            click_fig_center('data/img/developer/step_005.png')
        test_limit_recaptcha()

        dirpath = f'{os.environ.get("PATH_DOWNLOAD")}/audio.mp3'

        if os.path.exists(dirpath):
            os.remove(dirpath)

        recaptcha_reset = time_by_img(
            'data/img/developer/reset_recaptcha.png', 1)
        if recaptcha_reset == True:
            click_fig_center('data/img/developer/reset_recaptcha.png')

        audio_buttom = time_by_img('data/img/developer/step_006.png', 2)
        if audio_buttom == True:
            click_fig_center('data/img/developer/step_006.png')

        test_limit_recaptcha()
        try:
            time_by_img('data/img/developer/step_007.png')
            click_fig_center('data/img/developer/step_007.png')

            test_limit_recaptcha()

            time_by_img('data/img/developer/step_008.png')
            click_fig_left('data/img/developer/step_008.png')

            time_by_img('data/img/developer/step_009.png')
            click_fig_center('data/img/developer/step_009.png')

            time_by_img('data/img/developer/step_010.png')
            click_fig_left('data/img/developer/step_010.png')

            list_step_011 = ['data/img/developer/step_011.png',
                             'data/img/developer/step_011-1.png']
            for step_011 in list_step_011:
                try:
                    time_by_img(step_011, 2)
                    click_fig_center(step_011)
                except Exception as error:
                    print(f'[ERROR] {step_011} - {error}')

            phrase_regognize = get_text_by_audio(dirpath)
            print(f'[INFO] Recognize: {phrase_regognize}')

            if phrase_regognize != None:
                human_digite(phrase_regognize)
                list_step_012 = ['data/img/developer/step_012.png',
                                 'data/img/developer/step_012-1.png']
                for step_012 in list_step_012:
                    try:
                        time_by_img(step_012, 2)
                        click_fig_center(step_012)
                    except Exception as error:
                        print(f'[ERROR] {step_012} - {error}')

            pass_test = time_by_img(
                'data/img/developer/step_recaptcha_ok.png', 5)

        except Exception as error:
            print(f'[ERROR] Error in Recaptcha: {error}')
            time_by_img(back_page)
            click_fig_center(back_page)

        if os.path.exists(dirpath):
            os.remove(dirpath)

    return pass_test


# recaptcha_solver('data/img/developer/step_004.png')
