# Recaptcha solver

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat-square)](https://www.python.org/)
[![GitHub](https://img.shields.io/github/license/BrunoASNascimento/recaptcha_solver?style=flat-square)](LICENSE)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/BrunoASNascimento/recaptcha_solver.svg?logo=lgtm&logoWidth=18&style=flat-square)](https://lgtm.com/projects/g/BrunoASNascimento/recaptcha_solver/context:python)
[![PyPI](https://img.shields.io/pypi/v/recaptcha-solver?style=flat-square)](https://pypi.org/project/recaptcha-solver/)
[![wakatime](https://wakatime.com/badge/github/BrunoASNascimento/recaptcha_solver.svg?style=flat-square)](https://wakatime.com/badge/github/BrunoASNascimento/recaptcha_solver)

Resolve Recaptcha usando selenium e o pyautogui.

## Instalação:

`$ pip install recaptcha-solver`

## Parâmetros:

- **path_download [string]**: Local de download padrão do navegador.
- **[img_activate_recaptcha [string]](img/img_activate_recaptcha.png)**: Caminho da imagem que ativa a tela do Recaptcha.
- **[img_sound [string]](img/img_sound.png)**: Caminho da imagem que ativa a tela de som do Recaptcha.
- **[img_reset_recaptcha [string]](img/img_reset_recaptcha.png)**: Caminho da imagem que faz o reset do Recaptcha.
- **[img_download_recaptcha [string]](img/img_download_recaptcha.png)**: Caminho da imagem que abre a tela para download som do Recaptcha.
- **[img_error_recaptcha [string]](img/img_error_recaptcha.png)**: Caminho da imagem com erro do Recaptcha.
- **[img_options_sound [string]](img/img_options_sound.png)**: Caminho da imagem que abre a tela de opções para download som do Recaptcha.
- **[img_download_sound [string]](img/img_download_sound.png)**: Caminho da imagem que faz o download do som do Recaptcha.
- **[img_close_sound [string]](img/img_close_sound.png)**: Caminho da imagem que fecha a tela de download do som do Recaptcha.
- **[imgs_text_box [list]](img/imgs_text_box_001.png)**: Caminho da imagem que ativa a caixa de texto do Recaptcha.
- **[imgs_verify [list]](img/imgs_verify_001.png)**: Caminho da imagem do botão para verificação do Recaptcha.
- **[img_check [string]](img/img_check.png)**: Caminho da imagem com o OK do Recaptcha.
- **[img_back_page [string] (default=None)](img/img_back_page.png)**: Caminho da imagem para entrar novamente na página que contém o Recaptcha.

## Retorno:

Boll, caso `True` o Recaptcha foi quebrado com sucesso, caso `False`, o Recaptcha **NÃO** foi quebrado.

## Como usar:

- ### Google chrome debug:

  Para o Recaptcha não marcar o driver do selenium como um robô, é necessário iniciar o chrome com o seguinte comando:

  `$ "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8989 --user-data-dir="seu-local-para-salvar-dados"`

- ### Configurando o driver do selenium:

  É necessário passar alguns parâmetro no selenium para o correto funcionamento dele, os comandos são:

  ```
       chrome_options.add_experimental_option(
           'debuggerAddress',
           'localhost:8989'
       )
       chrome_options.add_argument('--ignore-certificate-errors')
       chrome_options.add_argument("--start-maximized")
       chrome_options.add_argument('--ignore-ssl-errors')
  ```

### Código de apoio:

Para um maior compreendimento de como utilizar a biblioteca, é possível ver o código [`test.py`](test.py), onde ocorre a quebra do Recaptcha no site [recaptcha/api2/demo](https://www.google.com/recaptcha/api2/demo).

## Desinstalar:

`$ pip uninstall recaptcha-solver`
