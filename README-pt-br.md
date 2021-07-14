# Recaptcha solver

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub](https://img.shields.io/github/license/BrunoASNascimento/recaptcha_solver)](LICENSE)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/BrunoASNascimento/recaptcha_solver.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/BrunoASNascimento/recaptcha_solver/context:python)

Resolve Recaptcha usando selenium e o pyautogui.

## Instalação:

`$ pip install recaptcha-solver`

## Parâmetros:

- **path_download [string]**: Local de download padrão do navegador.
- **img_activate_recaptcha [string]**: Caminho da imagem que ativa a tela do Recaptcha.
- **img_sound [string]**: Caminho da imagem que ativa a tela de som do Recaptcha.
- **img_reset_recaptcha [string]**: Caminho da imagem que faz o reset do Recaptcha.
- **img_download_recaptcha [string]**: Caminho da imagem que abre a tela para download som do Recaptcha.
- **img_error_recaptcha [string]**: Caminho da imagem com erro do Recaptcha.
- **img_options_sound [string]**: Caminho da imagem que abre a tela de opções para download som do Recaptcha.
- **img_download_sound [string]**: Caminho da imagem que faz o download do som do Recaptcha.
- **img_close_sound [string]**: Caminho da imagem que fecha a tela de download do som do Recaptcha.
- **imgs_text_box [list]**: Caminho da imagem que ativa a caixa de texto do Recaptcha.
- **imgs_verify [list]**: Caminho da imagem do botão para verificação do Recaptcha.
- **img_check [string]**: Caminho da imagem com o OK do Recaptcha.
- **img_back_page [string] (default=None)**: Caminho da imagem para entrar novamente na página que contém o Recaptcha.
