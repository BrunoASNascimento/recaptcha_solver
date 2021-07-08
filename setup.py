from setuptools import setup

with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
    name='log_kbots',
    version='0.0.3',
    author='Bruno Nascimento',
    author_email='bruno_freddy@hotmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['log_kbots'],
    url='https://github.com/kbots-dga-kroton/log_kbots',
    project_urls={
        'Código fonte': 'https://github.com/kbots-dga-kroton/log_kbots',
        'Download': 'https://github.com/kbots-dga-kroton/log_kbots/archive/main.zip'
    },
    license='MIT',
    keywords=['log_kbots', 'kbots', 'kroton'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization'
    ],
    python_requires='>=3.6'
)
