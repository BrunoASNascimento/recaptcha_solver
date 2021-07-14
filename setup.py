from setuptools import setup

with open("README.md", 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='recaptcha_solver',
    version='1.0.0',
    author='Bruno Nascimento',
    author_email='bruno_freddy@hotmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['recaptcha_solver', 'recaptcha_solver/click_img',
              'recaptcha_solver/human_style'],
    url='https://github.com/BrunoASNascimento/recaptcha_solver',
    project_urls={
        'Código fonte': 'https://github.com/BrunoASNascimento/recaptcha_solver',
        'Download': 'https://github.com/BrunoASNascimento/recaptcha_solver/archive/refs/heads/main.zip'
    },
    license='GPL',
    keywords=['recaptcha_solver', 'recaptcha'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization'
    ],
    python_requires='>=3.8'
)
