#!/usr/bin/env python3

from distutils.core import setup

setup(name='Telegram_bot',
      version='v0.0.1',
      description='Telegram fancy bot',
      author='Lyashenko Artem',
      author_email='CHANGEME',
      url='https://github.com/LyashenkoArtem/Telegram_bot',
      packages=['Da_Bot',],
      # packages=setuptools.find_packages(),
      install_requires=['pyTelegramBotAPI'],
      python_requires='>=3.9',
     )
