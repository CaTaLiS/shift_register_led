import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "shift_register_led",
    version = "0.1.0",
    author = "CaTaLiS",
    author_email = "catalis.dev@gmail.com",
    description = ("shift register 74HC595"),
    keywords = "shift register 74HC595 led",
    url = "https://github.com/CaTaLiS/shift_register_led",
    packages = ['shift_register_led', 'tests'],
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
    ],
)