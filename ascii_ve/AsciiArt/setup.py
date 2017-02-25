from setuptools import setup

setup(name='AsciiArt',
    version='0.1.dev',
    description='Ascii "art" from images',
    author='Momo',
    packages=['asciiart'],
    install_requires=['pillow', 'requests'])